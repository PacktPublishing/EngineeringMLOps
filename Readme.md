# Engineering MLOps

<a href="https://www.packtpub.com/product/engineering-mlops/9781800562882"><img src="https://static.packt-cdn.com/products/9781800562882/cover/smaller" alt="Book Name" height="256px" align="right"></a>

This is the code repository for [Engineering MLOps](https://www.packtpub.com/product/engineering-mlops/9781800562882), published by Packt.

**Rapidly build, test, and manage production-ready machine learning life cycles at scale**

## What is this book about?
MLOps is a systematic approach to building, deploying, and monitoring machine learning (ML) solutions. It is an engineering discipline that can be applied to various industries and use cases. This book presents comprehensive insights into MLOps coupled with real-world examples to help you to write programs, train robust and scalable ML models, and build ML pipelines to train and deploy models securely in production.
This book covers the following exciting features: 
* Formulate data governance strategies and pipelines for ML training and deployment
* Get to grips with implementing ML pipelines, CI/CD pipelines, and ML monitoring pipelines
* Design a robust and scalable microservice and API for test and production environments
* Curate your custom CD processes for related use cases and organizations
* Monitor ML models, including monitoring data drift, model drift, and application performance
* Build and maintain automated ML systems

If you feel this book is for you, get your [copy](https://www.amazon.com/Engineering-MLOps-Rapidly-production-ready-learning/dp/1800562888) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter06.

The code will look like the following:
```
ws = Workspace.from_config()
model1 = Model(ws, 'support-vector-classifier')
model2 = Model(ws, 'scaler')
service = Model.deploy(workspace=ws,
                       name='weatherprediction',
                       models=[model1, model2],
                       inference_config=inference_config,
                       deployment_config=aciconfig)
service.wait_for_deployment(show_output=True)

```

**Following is what you need for this book:**
This MLOps book is for data scientists, software engineers, DevOps engineers, machine learning engineers, and business and technology leaders who want to build, deploy, and maintain ML systems in production using MLOps principles and techniques. Basic knowledge of machine learning is necessary to get started with this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-13).

### Software and Hardware List

| Chapter  | Software required                                                    | OS required                        |
| -------- | ---------------------------------------------------------------------| -----------------------------------|
| 1-13     | Python, Git, Microsoft Azure, Azure ML Service, MLFlow, Azure DevOps | Windows, Mac OS X, and Linux (Any) |
| 8        | Docker, Fast API                                                     | Windows, Mac OS X, and Linux (Any) |
| 9        | Locust.io                                                            | Windows, Mac OS X, and Linux (Any) |
| 10       | Kubernetes                                                           | Windows, Mac OS X, and Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781800562882_ColorImages.pdf).

### Related products <Other books you may enjoy>
* Interpretable Machine Learning with Python [[Packt]](https://www.packtpub.com/product/interpretable-machine-learning-with-python/9781800203907) [[Amazon]](https://www.amazon.com/Interpretable-Machine-Learning-Python-hands/dp/180020390X)

* Mastering Azure Machine Learning [[Packt]](https://www.packtpub.com/product/mastering-azure-machine-learning/9781789807554) [[Amazon]](https://www.amazon.com/Mastering-Azure-Machine-Learning-end-ebook/dp/1789807557)
  
## Errata 
 * Page 20 (Under Deploy):  **Figure 1.12 depicts the deploy pipeline, which has two components** _should be_ **Figure 1.11 depicts the deploy pipeline, which has two components**

## Get to Know the Author
**Emmanuel Raj**
is a Finland-based Senior Machine Learning Engineer with 6+ years of industry experience. He is also a Machine Learning Engineer at TietoEvry and a Member of the European AI Alliance at the European Commission. He is passionate about democratizing AI and bringing research and academia to industry. He holds a Master of Engineering degree in Big Data Analytics from Arcada University of Applied Sciences. He has a keen interest in R&D in technologies such as Edge AI, Blockchain, NLP, MLOps and Robotics. He believes "the best way to learn is to teach", he is passionate about sharing and learning new technologies with others.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781800562882">https://packt.link/free-ebook/9781800562882 </a> </p>