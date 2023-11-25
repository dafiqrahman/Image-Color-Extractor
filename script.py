from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def import_image(image):
    image = image.resize((100, 100))
    image = np.array(image)
    image_reshape = image.reshape(-1, 3)
    return image_reshape


def cluster_image(image_reshape, n_clusters=5):
    df = pd.DataFrame(image_reshape, columns=['red', 'green', 'blue'])
    kmeans = KMeans(n_clusters=n_clusters, n_init="auto")
    kmeans.fit(df)
    df['cluster'] = kmeans.predict(df)
    return df, kmeans


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def plot_colors(model):
    centers = model.cluster_centers_
    n_clusters = len(centers)
    centers = np.array(centers, dtype='uint8')
    normalized_centers = centers / 255.
    color_data = [[[i]] for i in normalized_centers]
    nrow = n_clusters//2
    ncol = n_clusters//nrow + n_clusters % nrow
    fig, axs = plt.subplots(nrow, ncol)
    # auto adjust the layout
    plt.tight_layout()
    fig.patch.set_alpha(0.)
    for i, color in enumerate(color_data):
        rgb = np.array(color)

        # Plot a single pixel with the specified color
        axs[i//ncol, i % ncol].imshow(rgb)
        axs[i//ncol, i % ncol].axis('off')
        axs[i//ncol, i % ncol].set_title(rgb2hex(*centers[i]))
        # axs[i].imshow(rgb)
        # axs[i].axis('off')  # Turn off axis labels
        # axs[i].set_title(rgb2hex(*centers[i]))
    # set remaining axes invisible
    for i in range(n_clusters, nrow*ncol):
        axs[i//ncol, i % ncol].set_visible(False)
        # axs[i].set_visible(False)
    plt.axis('off')
    plt.tight_layout()
    # transparent background
    return (fig, axs)


def main(image, n_colors):
    image_reshape = import_image(image)
    df, model = cluster_image(image_reshape, n_colors)
    return plot_colors(model)
