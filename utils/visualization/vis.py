import matplotlib.pyplot as plt
import numpy as np

def plot_loss(train_loss, val_loss, title='loss'):
    x = np.arange(len(train_loss)) + 1
    
    plt.figure(figsize=(15,5))
    plt.subplot(1, 2, 1)
    plt.title(title)
    plt.plot(x, train_loss, label='train')
    plt.plot(x, val_loss, label='val')
    plt.ylabel(title)
    plt.xlabel('epoch')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.title(f'Log({title})')
    plt.plot(x, np.log(train_loss), label='train')
    plt.plot(x, np.log(val_loss), label='val')
    plt.ylabel(f'Log({title})')
    plt.xlabel('epoch')
    plt.legend()
    
    plt.show()
    
def plot_some_predictions(images, density_maps, preds):
    num_images = len(images)
    for i in range(num_images):
        plt.figure(figsize=(15, 12))
        plt.subplot(num_images, 3, 1)
        plt.title('initial image')
        plt.imshow(images[i])

        plt.subplot(num_images, 3, 2)
        plt.title(f'gt density map: {density_maps[i].sum():.2f}')
        plt.imshow(density_maps[i], cmap='jet')
        plt.colorbar(fraction=0.045, pad=0.04)
        plt.axis('off')

        plt.subplot(num_images, 3, 3)
        pred = preds[i].squeeze()
        plt.title(f'pred density map: {pred.sum():.2f}')
        plt.imshow(pred, cmap='jet')
        plt.colorbar(fraction=0.045, pad=0.04)
        plt.axis('off')