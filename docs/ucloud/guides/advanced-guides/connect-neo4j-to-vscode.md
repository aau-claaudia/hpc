# How to Connect Neo4j to VS Code on UCloud

## Overview

This solution demonstrates how to harness UCloud aau/k8's internal networking to create a robust, distributed architecture. By connecting two instances, you can run a dedicated Neo4j database server on one instance while running your applications (LangGraph, LangChain, and LLM) on another instance. This approach gives you the best of both worlds: persistent, reliable database storage and flexible, scalable application deployment.

**Universal application**: While this guide uses Neo4j as an example, the same connection procedure applies to many other services such as PostgreSQL, MySQL, Redis, MongoDB or any application that needs to communicate between UCloud instances.

## Prerequisites

- Access to UCloud with AAU/K8 instances
- Both instances should be in the same UCloud project for network access

## Step-by-Step Solution

### Step 1: Start Neo4j Server

1. Start your Neo4j server instance on UCloud
2. Choose an appropriate instance size for your database needs

### Step 2: Open the terminal and install required tools

```bash
# Update package lists
sudo apt update
```

```bash
# Install iproute2 for network configuration
sudo apt install iproute2
```

### Step 3: Find Your Instance IP

```bash
# Find your instance's internal IP address
ip addr show | grep "inet " | grep -v 127.0.0.1
```

Look for a line like: `inet 10.14.11.155/32` - this is your internal IP address.

### Step 4: Start VS Code and Connect

1. Start VS Code on your application instance
2. Activate "connect jobs" at the bottom by providing a host name and select the database server. 
3. 

### Step 5: Connect via Python Driver

Use the following Python code to connect to your Neo4j database:

```python
from neo4j import GraphDatabase

# Replace with your Neo4j instance's internal IP address
uri = "bolt://YOUR_INSTANCE_IP:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "ucloud"))

with driver.session() as session:
    result = session.run("RETURN 1 AS test")
    for record in result:
        print(record["test"])
```

**Important**: Remember to change `"bolt://YOUR_INSTANCE_IP:7687"` to your actual IP address from the Neo4j server, and update the username and password if you have changed them.

**Example**: If your Neo4j instance has the internal IP address `10.14.11.155/32`, your connection string would be:
```python
uri = "bolt://10.14.11.155:7687"
```

## Troubleshooting

If the connection doesn't work:

1. Verify both instances are in the same UCloud project
2. Check that Neo4j is running on the server instance
3. Ensure the internal IP address is correct
4. Test the connection with the provided Python code
5. Make sure to start the instances in the correct order with Neo4j first and VS code afterwards.

## Benefits of This Approach

- **Scalability**: Run your database and applications on optimally-sized instances
- **Reliability**: Persistent database storage that survives instance restarts
- **Flexibility**: Easy to scale individual components without affecting others
- **Performance**: Dedicated resources for both database and application workloads
- **Cost Efficiency**: Optimize resource allocation for different types of workloads

## Conclusion

This setup demonstrates the power of UCloud's networking capabilities, enabling you to create sophisticated, distributed computing environments. By connecting two instances, you can build robust, scalable applications that leverage persistent databases while maintaining the flexibility to deploy and manage your workloads independently.

**Beyond Neo4j**: The networking principles and connection procedures demonstrated in this guide are universal. Whether you're connecting to Neo4j, PostgreSQL, Redis, or any other service, the same approach applies. This makes UCloud an excellent platform for building complex, distributed architectures with any combination of databases, APIs, and applications.

**Note on Ports**: Different applications use different default ports. For example, Neo4j uses port 7687, PostgreSQL typically uses port 5432, and Redis uses port 6379. You can find the specific port information for each application in the [UCloud application documentation](https://docs.cloud.sdu.dk/index.html).
