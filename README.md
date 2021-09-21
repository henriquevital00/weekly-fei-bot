# weekly-fei-bot

# Introduction
This objective of this project is to automate the daily feedback of the [FEI](https://portal.fei.edu.br/) college.

# How to run on [AWS](https://aws.amazon.com/)
In order to run the bot on aws follow the next steps:

- Go to functions in Lambda page
- Click in **create function button** on top right
  ![](images/createLambdaFunction.png)
- Click in **Layers**, click in **Create a layer**
- Insert a name and upload the file **chrome_headless.zip**, this file is in the repository that you cloned
  ![](images/createLambda.png)
- Add the layer
  ![](images/addLayer.png)

- Copy the code of [bot.py](https://github.com/henriquevital00/weekly-fei-bot/blob/main/bot.py) and paste in code source
  ![](images/codeSource.png)

- Go to configuration in General Configuration change the **Timeout to 3min** and change the **memory to 1000**