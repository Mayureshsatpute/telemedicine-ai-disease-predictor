from tensorflow.keras.layers import Input, Dense, Dropout, BatchNormalization, LeakyReLU
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ReduceLROnPlateau

# Input
inputs = Input(shape=(X_train.shape[1],))

# Layer 1
x = Dense(128, kernel_regularizer='l2')(inputs)
x = BatchNormalization()
x = LeakyReLU()(x)
x = Dropout(0.4)(x)

# Layer 2
x = Dense(64, kernel_regularizer='l2')(x)
x = BatchNormalization()
x = LeakyReLU()(x)
x = Dropout(0.3)(x)

# Layer 3
x = Dense(32, kernel_regularizer='l2')(x)
x = BatchNormalization()
x = LeakyReLU()(x)

# Output
outputs = Dense(1, activation='sigmoid')(x)

# Model
model = Model(inputs, outputs)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Callbacks
early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.3, patience=5, min_lr=1e-6)

# Train
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=150,
    batch_size=16,  # Try 16
    callbacks=[early_stop, reduce_lr],
    verbose=1
)
