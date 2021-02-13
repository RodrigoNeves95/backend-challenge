# backend-challenge
Repository with backend challenge

# Challenge description

DataHow backend coding challenge
In this coding challenge, for which you should not invest more than 3 hours, you will be developing a micro-service.

Your team has been asked by business to provide them with a dashboard that shows how many unique IP addresses have been visiting the company's website. The DevOps engineer in your team says, he can easily use Prometheus and Grafana to provide the dashboard, but you need to provide a micro-service to count the unique IP addresses. The DevOps engineer can configure the ingress controller to send you a structured log message in JSON format for each page request in the following format:

``````
{ "timestamp": "2020-06-24T15:27:00.123456Z", "ip": "83.150.59.250", "url": ... }
``````

Each log entry is sent to your web-service via HTTP/1.1 POST to
http://your-service:5000/logs . For simplicity, you are only supposed to count how many unique IP addresses have been logged since the start of the service. Keep in mind that there might be potentially thousands of visitors per second. Provide the cumulative count as custom metric to a Prometheus server. Prometheus will periodically scrape metrics from your service at http://your-service:9102/metrics .

You have 3 hours to implement, benchmark, and document your solution. Decide on the order in which you implement the requirements. We value clean and tested code over fully implemented requirements. Also, we appreciate the use of smart algorithms and 3rd party libraries to achieve your goal. Finally, upload your solution to a public Git repository like GitHub.

### Requirements:
 * Time limit for assignment: 3 hours
 * Listen on ports :5000 and :9102
 * Receive JSON logs on :5000/logs
 * Serve Prometheus metrics on :9102/metrics
 * Compute number of unique IP addresses in logs since service start
 * Create custom Prometheus metric "unique_ip_addresses"
 * Publish your result in public Git repository
### NOT required:
 * Persistence
 * Validate inputs (assume the logs are well formatted)
### Bonus:
 * Benchmark your API with a tool like siege or gobench
 * Preferred languages Go, Rust, TypeScript
 * Develop your code in logical increments and document those via git commit messages
 * Test driven development
 * Evaluation criteria:
 * Clean code
 * Memory usage
 * Performance
 * Unit tests
 * Git history and commit messages

***

# Initial Approach (before implementation)

Setup a fastAPI app to receive POST requests on :5000 and store necessary data in memory. Use prometheus_client to serve metrics on port :9102/metrics. Use docker to serve everything together with port 5000 and 9102 exposed.

# Final Approach 

The current implementation is described above. The only thing worth to add is we are using a middleware to register Prometheus metrics automatically and serve on ``/metrics``

### How to run

To deploy the microservice run `make deploy`. This will build a docker image and deploy it with ports `5000` and `9102` exposed. After that receiving JSON logs on ``:5000/logs`` and read metrics on ``:9102/metrics`` should be working.

There is two files to make mock requests. This was used for development purposes and not a final goal. That being said if you want to use them, make sure that you have the necessary dependencies.

`python mock_logs_request.py --number int --port int --host str`

* `--number` Number of random IPs POST request to make
* `--port`   Target Port. Default = 5000
* `--host`   Target Host. Default = "localhost" 

`python mock_metrics_request.py int --port int --host str `
* `--port`   Target Port. Default = 5000
* `--host`   Target Host. Default = "localhost" 

### What is missing

* Unit Tests
* Benchmark
