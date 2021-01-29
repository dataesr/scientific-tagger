sh docker_push_ext.sh
kubectl delete deployment scientific-tagger-web
kubectl delete deployment scientific-tagger-worker
kubectl apply -k k8s
kubectl get pods
