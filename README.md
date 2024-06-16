# Challenge DevOps N5 Now

## **CI/CD**

### **Job - buildImage**

* En esta fase se construye la imagen y se guarda en el servicio Amazon Elastic Container Registry

### **Job - deploy**

* En esta fase se despliega la aplicaciòn en Amazon Elastic Container Service.
* Se agrega un paso adicional donde termina una task para poder liberar el container.

![CI/CD](./images/devops_challenge_n5now.png)


## **PRUEBAS**

* Se evidencia la ejecución de los workflows en GitHub
* Se evidencia los eventos en AWS ECS

![gha_challenge_n5now](./images/gha_challenge_n5now.png)

![ecs_events_challenge_n5now](./images/ecs_events_challenge_n5now.png)

### Al momento de lanzar el workflow desde el branch **develop**

![app-develop](./images/print-app-develop.png)

### Al momento de lanzar el workflow desde el branch **testing**

![app-testing](./images/print-app-testing.png)


## **INFRAESTRUCTURA**

* Mencionar que la infraesctructura se creó por IaC mediante Terraform.

![iac_challenge_n5now](./images/iac_challenge_n5now.png)


## **REFERENCIAS**

* https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-amazon-elastic-container-service
* https://github.com/aws-actions/amazon-ecr-login
* https://github.com/aws-actions/amazon-ecs-render-task-definition
* https://github.com/aws-actions/amazon-ecs-deploy-task-definition