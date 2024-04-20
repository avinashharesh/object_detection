# Image Object Detection Web Service Within A Containerised Environment In Clouds
## Description and Objective
This project aims to build a web-based system that we call CloudDetect. It will allow end-users to
send an image to a web service hosted by Docker containers and receive a list of objects detected in their
uploaded image. The project will make use of the YOLO (You Only Look Once) library, a state-of-theart real-time object detection system, and OpenCV (Open-Source Computer Vision Library) to perform
the required image operations/transformations. Both YOLO and OpenCV are Python-based open-source
computer vision and machine learning software libraries. The web service will be hosted as containers in a
Kubernetes cluster. Kubernetes will be used as the container orchestration system. The object detection
web service is also designed to be a RESTful API that can use Python’s Flask library. We are interested
in examining the performance of CloudDetect by varying the rate of requests sent to the system (demand)
using load generation tools like Locust and the number of existing Pods within the Kubernetes cluster
(resources).

This project has the following objectives
- Writing a python web service that accepts images in JSON object format, uses YOLO and OpenCV
to process images, and returns a JSON object with a list of detected objects.
- Building a Docker Image for the object detection web service.
- Creating a Kubernetes cluster on virtual machines (instances) in the Oracle Cloud Infrastructure.
- Deploying a Kubernetes service to distribute inbound requests among pods that are running the
object detection service.

## Docker
![Docker](https://www.docker.com/wp-content/uploads/2021/11/docker-containerized-appliction-blue-border_2.png)
A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

Container images become containers at runtime and in the case of Docker containers – images become containers when they run on Docker Engine. Available for both Linux and Windows-based applications, containerized software will always run the same, regardless of the infrastructure. Containers isolate software from its environment and ensure that it works uniformly despite differences for instance between development and staging.

Docker containers that run on Docker Engine:
- Standard: Docker created the industry standard for containers, so they could be portable anywhere
- Lightweight: Containers share the machine’s OS system kernel and therefore do not require an OS per application, driving higher server efficiencies and reducing server and licensing costs
- Secure: Applications are safer in containers and Docker provides the strongest default isolation capabilities in the industry

## Kubernetes
![Kubernetes](https://images.ctfassets.net/w1bd7cq683kz/5Ex6830HzBPU5h8Ou8xQAB/2c948105fc10094348203bec6c1eab04/Kubernetes_20architecture_20diagram.png)
A Kubernetes (K8s) cluster is a group of computing nodes, or worker machines, that run containerized applications. Containerization is a software deployment and runtime process that bundles an application’s code with all the files and libraries it needs to run on any infrastructure. Kubernetes is an open source container orchestration software with which you can manage, coordinate, and schedule containers at scale. Kubernetes places containers into pods and runs them on nodes. A Kubernetes cluster has, at a minimum, a master node running a container pod and a control plane that manages the cluster. When you deploy Kubernetes, you are essentially running a Kubernetes cluster.

To understand a Kubernetes cluster, you first need to understand the fundamentals of containerization with Kubernetes. 

A container is a single application or microservice packaged with its dependencies, runnable as a self-contained environment and application in one. Modern applications adopted distributed microservices architecture where every application includes hundreds or even thousands of discrete software components that run independently. Every component (or microservice) performs a single independent function to enhance code modularity. By creating independent containers for each service, applications can be deployed and distributed across a number of machines. You can scale individual microservice workloads and computation capabilities up or down to maximize application efficiency.

Kubernetes is open source container orchestration software that simplifies the management of containers at scale. It can schedule, run, start up and shut down containers, and automate management functions. Developers get the benefits of containerization at scale without the administration overheads.

Kubernetes cluster management is the term for managing multiple Kubernetes clusters at scale. As an example, consider a development environment—the team may require test, development, and production clusters that each run across multiple distributed on-site and cloud-based physical and virtual machines.

To manage multiple different types of clusters together, you need to be able to perform cluster operations such as creation and destruction, in-situ updates, maintenance, reconfiguration, security, cluster data reporting, and so on. Multi-cluster management can be achieved through a combination of Kubernetes services, specialized tools, configurations, and best practices.

## Working
URL for object detection:
[Object Detection]()

For the app to work
1. Open Postman
2. Set the type of request as POST
3. Set the body to raw-JSON
4. Format of json file should be {"images":[{"id":id_image1,"image":base64_encoded_image1},{"id":id_image2,"image":base64_encoded_image2},....]}
