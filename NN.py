def NNT2():
    import tensorflow as tf
    from tensorflow import keras
    import numpy as np
    # print("Запуск скрипта")

    q = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], dtype=float)
    a = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], dtype=float)
    t = np.array([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 55, 67, 676, 88, 99, 33, 789, 1244, 122], dtype=float)
    # print("Тренеровочные и проверочные списки загруженны")

    l0 = tf.keras.layers.Dense(units=2, input_shape=[1])
    l1 = tf.keras.layers.Dense(units=1, input_shape=[2])
    model = tf.keras.Sequential([l0, l1])
    # print("Модель создана")

    model.compile(loss='mean_squared_error',
                  optimizer=tf.keras.optimizers.Adam(0.1))
    # print("Модель скомпилировна")

    history = model.fit(q, a, epochs=400, verbose=False)
    # print("Модель обучена")

    predictions = model.predict(t)
    # print("Значение принято")
    # print(predictions)
    return predictions