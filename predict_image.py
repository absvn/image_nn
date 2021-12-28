## predict image from the model

def predictImage(filename):
    img1 = image.load_img(filename,target_size=(150,150))
    
    plt.imshow(img1)
 
    Y = image.img_to_array(img1)
    
    X = np.expand_dims(Y,axis=0)
    val = model.predict(X)
    print(val)
    if val == 1:
        
        plt.xlabel("airplane",fontsize=30)
        
    
    elif val == 0:
        
        plt.xlabel("ufo",fontsize=30)
        
        
        
 predictImage('/Users/abhinavsingh/Desktop/predict_image/8.jpg')
