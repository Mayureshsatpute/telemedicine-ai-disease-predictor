import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

# Load and preprocess data
df = pd.read_csv("heart dataset122.csv")
df["chol_age_ratio"] = df["chol"] / df["age"]
df["bp_age_ratio"] = df["trestbps"] / df["age"]
df = df.drop(columns=["id", "dataset"])
df = pd.get_dummies(df)

# Target: Binary classification
y = df["num"].apply(lambda x: 0 if x == 0 else 1)
X = df.drop("num", axis=1)

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Handle imbalance
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_scaled, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

# Neural Network
model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    BatchNormalization(),
    Dropout(0.3),
    
    Dense(128, activation='relu'),
    BatchNormalization(),
    Dropout(0.3),

    Dense(64, activation='relu'),
    BatchNormalization(),
    Dropout(0.2),

    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Early stopping to avoid overfitting
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Train
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=150,
    batch_size=32,
    callbacks=[early_stop],
    verbose=1
)

# Evaluate
y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype(int)

acc = accuracy_score(y_test, y_pred_classes)
print(f"\n✅ Final Accuracy: {acc * 100:.2f}%\n")
print("🔍 Classification Report:\n", classification_report(y_test, y_pred_classes))
print("📊 Confusion Matrix:\n", confusion_matrix(y_test, y_pred_classes))

# Plot training history
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.title("Model Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
