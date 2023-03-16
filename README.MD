# MLE PROJECT: OPTIMIZE IMAGE CLASSIFICATION

<p align="center">
    <img src='https://storage.googleapis.com/protonx-cloud-storage/transformer/protonx-transf.png' width=200 class="center">
</p>

Slide about project: [click here](https://docs.google.com/presentation/d/1FbZp18rV2AMBOPFUg0yYb_3h96vZ2uNd/edit#slide=id.p1)

Authors:

- Github: https://github.com/minhhiepcr
- Email: truongminhhiep246@gmail.com
- Github: https://github.com/Johnx69
- Email: hoanganh692004@gmail.com
- Github: https://github.com/vinhtran26092001
- Email: tranvinh26092001@gmail.com

Advisors:

- Github: https://github.com/bangoc123
- Email: bangoc.gdg@gmail.com

## I. Set up environment

The problem here is how we can create microservice to classify cat & dog image. To solve this problem we use the Kaggle's dataset and MobileNet.

![alt text for screen readers](https://camo.githubusercontent.com/f0fe57a3540c293e21dcadff0cf5dedf3aaaea16509613822ee713fd40228a91/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f313833382f312a6f4233533579484868766f75674a6b50587563386f672e676966 "Text to show on mouseover")

We use Google colab to download dataset, pretrained model, fine-tune and export it to ONNX model after complete training process. You can find the our notebook in [here](./notebook/Dogs_Cats_MobileNet.ipynb).

The dataset can be found [here](https://www.kaggle.com/competitions/dogs-vs-cats/data)

## II. Training Process

This is the result of training process

```sh
Epoch 10/20
32/32 [==============================] - 28s 900ms/step - loss: 0.3010 - accuracy: 0.9719 - val_loss: 0.0556 - val_accuracy: 0.9797
Epoch 11/20
32/32 [==============================] - 28s 898ms/step - loss: 0.2545 - accuracy: 0.9688 - val_loss: 0.5366 - val_accuracy: 0.9625
Epoch 12/20
32/32 [==============================] - 28s 901ms/step - loss: 0.3735 - accuracy: 0.9703 - val_loss: 0.2056 - val_accuracy: 0.9781
Epoch 13/20
32/32 [==============================] - 28s 903ms/step - loss: 0.3763 - accuracy: 0.9719 - val_loss: 0.2275 - val_accuracy: 0.9750
Epoch 14/20
32/32 [==============================] - 29s 907ms/step - loss: 0.1343 - accuracy: 0.9875 - val_loss: 0.1534 - val_accuracy: 0.9766
Epoch 15/20
32/32 [==============================] - 29s 907ms/step - loss: 0.1849 - accuracy: 0.9875 - val_loss: 0.2573 - val_accuracy: 0.9719
Epoch 16/20
32/32 [==============================] - 28s 902ms/step - loss: 0.1530 - accuracy: 0.9859 - val_loss: 0.3693 - val_accuracy: 0.9734
Epoch 17/20
32/32 [==============================] - 28s 903ms/step - loss: 0.1701 - accuracy: 0.9844 - val_loss: 0.1868 - val_accuracy: 0.9812
Epoch 18/20
32/32 [==============================] - 29s 906ms/step - loss: 0.0948 - accuracy: 0.9906 - val_loss: 0.1464 - val_accuracy: 0.9812
Epoch 19/20
32/32 [==============================] - 29s 905ms/step - loss: 0.2519 - accuracy: 0.9828 - val_loss: 0.1669 - val_accuracy: 0.9797
Epoch 20/20
32/32 [==============================] - 29s 917ms/step - loss: 0.2726 - accuracy: 0.9859 - val_loss: 0.2805 - val_accuracy: 0.9734
```

After training model, we convert it to ONNX model. The following table will compare the result of two models.

|                    | MobileNet (.h5 format) | MobileNet (.onnx format) |
| ------------------ | ---------------------- | ------------------------ |
| Train accuracy     | 98.59%                 | 93.10%                   |
| Validation accuray | 97.34%                 | 92.36%                   |
| Model size         | 13MB                   | 12.41MB                  |

## III. Microservice

In this session, we use Flask framework to write microservice and containerize it by using Docker. All code can be found in [microservice](./microservice/) folder.

Tutorial to start the microservice:

Step 1:

```
cd microservice/
```

Step 2: Install related packages

```
python -m pip install -r requirements.txt
```

Step 3: Start microservice:

```sh
python app.py
```

In the local, you can see the service run in port 9000. You can use http://localhost:9000/api/detect to send test request.

Tutorial to deploy docker on DigitalOcean

Step 1: Containerize to docker image

```sh
sudo docker build -t [IMAGE NAME]:[TAG OF IMAGE] .
```

Note that, IMAGE NAME is suitable with your repo on DockerHub.

Step 2: Push image to DockerHub

```sh
sudo docker push [IMAGE NAME]:[TAG OF IMAGE]
```

Step 3: Create Droplets on DigitalOcean.

Step 4: SSH to Droplets and pull image from DockerHub

```sh
sudo docker pull [IMAGE NAME]:[TAG OF IMAGE]
sudo docker run -it -d -p 80:9000 --name [CONTAINER NAME] [IMAGE NAME]:[TAG OF IMAGE]
```

Step 5: Create Load Balancing and connect to all your droplets.

Step 6: Use public ip of Load Balancing to send request

## IV. Result of microservice

The sample of the request:

```json
{
  "image_file": [image]
}
```

The response after sending request to the server.

```json
{
  "message": "Successfully",
  "result": "dog"
}
```
