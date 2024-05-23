from keras.models import Sequential
import gc
from keras import backend as K



# Crear el modelo
model = Sequential()

# ... construir y entrenar el modelo ...

# Borrar el modelo
del model

# Limpiar la sesión
K.clear_session()
gc.collect()