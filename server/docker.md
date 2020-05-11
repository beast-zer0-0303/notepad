# docker

## コマンド

```
#network 一覧
docker network ls

#network構成確認
docker network inspect bridge

#network作成
docker network create -d bridge debian_web_nw

#network 確認
docker network inspect debian_web_nw


```

docker network create -d bridge debian_web_nw

docker run -it --name containername -h hostname --net=debian_web_nw --ip=192.198.160.10 ubuntu bash
