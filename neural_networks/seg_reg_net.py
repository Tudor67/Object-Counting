from keras.layers import *
from keras.models import *
from keras.optimizers import *


def encoder(inputs, params):
    # down1
    conv1 = Conv2D(32, 3, **params)(inputs)
    pool1 = MaxPooling2D(2, 2)(conv1)
    
    # down2
    conv2 = Conv2D(64, 3, **params)(pool1)
    pool2 = MaxPooling2D(2, 2)(conv2)
    
    # down3
    conv3 = Conv2D(128, 3, **params)(pool2)
    pool3 = MaxPooling2D(2, 2)(conv3)
    
    # bottleneck
    conv4 = Conv2D(512, 3, **params)(pool3)
    
    return conv4


def decoder(enc, params):
    # up1
    up1 = UpSampling2D(interpolation='bilinear')(enc)
    conv5 = Conv2D(128, 3, **params)(up1)
    
    # up2
    up2 = UpSampling2D(interpolation='bilinear')(conv5)
    conv6 = Conv2D(64, 3, **params)(up2)
    
    # up3
    up3 = UpSampling2D(interpolation='bilinear')(conv6)
    conv7 = Conv2D(32, 3, **params)(up3)
    conv8 = Conv2D(1, 3, padding='same', kernel_initializer='he_normal')(conv7)
    
    return conv8


def SegRegNet(input_shape=(None, None, 3),
              seg_loss_name='binary_crossentropy',
              reg_loss_name='logcosh',
              loss_weights=[0.5, 0.5],
              learning_rate=1e-3,
              pretrained_weights=None):
    
    # common params
    params = {
        'padding': 'same',
        'activation': 'relu',
        'kernel_initializer': 'he_normal'
    }
    
    # input
    inputs = Input(input_shape)
    
    # encoder
    enc = encoder(inputs, params)
    
    # decoders
    seg_dec = Activation('sigmoid')(decoder(enc, params))
    reg_dec = decoder(enc, params)
    
    # build the model
    model = Model(inputs=inputs, outputs=[seg_dec, reg_dec])
    model.compile(optimizer=Adam(lr=learning_rate),
                  loss=[seg_loss_name, reg_loss_name],
                  loss_weights=loss_weights)
    
    if pretrained_weights is not None:
        model.load_weights(pretrained_weights)
    
    return model