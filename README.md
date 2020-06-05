# mnist_sample_api
Sample REST API to predict MNIST classes (built on Google App Engine )

# Reference
https://qiita.com/fam_taro/items/1464c42324f15d7b8223

# how to use
(to run api on local)

1. 

```
$ source mnist_env/bin/activate
```

2. 

```
$ python3 app.py
``` 

3. 
```
$ curl http://XXXX:5000/predict -X POST -H 'Content-Type:application/json' -d '{"feature":[1, 0, 0, 1]}' 
```

(to deploy)

1. install gcloud-sdk

2. create GCP project on google cloud console

3. back to local, run below commands

```
$ gcloud init
```

```
$ gcloud app deploy
```

4. 
```
$ curl http://<application name>/predict -X POST -H 'Content-Type:application/json' -d '{"feature":[1, 0, 0, 1]}' 
```