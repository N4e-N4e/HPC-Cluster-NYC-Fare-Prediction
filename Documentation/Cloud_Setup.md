# Nautilus Setup:

Access to Nautilus was established via the JupyterHub interface using CILogon, which enables secure login with institutional credentials. For direct access to the cluster, an NRP account was created, followed by a request for access to the namespace gp-engine-mizzou-dsa-cloud.
Additionally, the Kubernetes configuration file was downloaded from the NRP portal, which was then modified and deployed to the .kube/config location, allowing the JupyterHub environment to communicate with the cluster. To interact with the cluster, kubectl command-line tools were used.

---------------------------------------------------------------------------------------------------------------------------------------

## Step-by-Step Access Process

Step 1: Initial Authentication

Navigate to the Nautilus JupyterHub URL and click "Sign in with CILogon". Link: https://gp-engine.nrp-nautilus.io/ 


Step 2: Choose Your Identity Provider

CILogon will present you with authentication options. Select either:

- GitHub: Uses your GitHub account credentials
- Google: Uses your Google account credentials
- Institutional Login: May be available depending on your university affiliation


Step 3: Container Environment Selection

After successful authentication, you'll be presented with computing environment options. Select: "Stack Datascience + K8s"


Step 4: JupyterLab Interface

Once your container starts, you'll see the full JupyterLab interface.

-------------------------------------------------------------------------------------------------------------------------------------

## Direct Cluster Access - Advanced Kubernetes Operations

Step 1: NRP Portal Registration

Begin by creating your NRP account:

- Navigate to the NRP Portal
- Click "Login" in the top-right corner
- Use the same authentication method you used for JupyterHub access
- Complete any required profile information


Step 2: Request Namespace Access

Kubernetes uses namespaces to organize and isolate resources between different projects and users.

Request you IT Admin, instructor or TA to be added to the namespace. 


Step 3: Command-Line Tools Installation (kubectl)

kubectl is the primary command-line tool for interacting with Kubernetes clusters.

- If using JupyterHub: Skip this step - kubectl is pre-installed.
- For local machine setup: Follow the official installation guide for your operating system (Windows, macOS, or Linux). Link: https://kubernetes.io/docs/tasks/tools/


Step 4: Obtain Your Kubernetes Configuration

The Kubernetes configuration file contains credentials and connection information for accessing the cluster.

Process:

- Return to the NRP documentation portal
- Locate the section "Cluster access via kubectl"
- Click "Download Config File"
- Save the file (typically named config) to your computer


Step 6: Modify Configuration for JupyterHub Environment

Important: This step is only necessary when using JupyterHub due to its headless (no graphical interface) environment.

JupyterHub containers run without a traditional desktop environment, so we need to modify the authentication flow:

Process:

- Open the config file by double-clicking it in JupyterHub
- Locate the section containing authentication parameters (near the end of the file)
- Find the line with --token-cache-storage=keyring
- Replace keyring with disk
- Add these two additional parameters:
    - --grant-type=device-code
    - --skip-open-browser


Step 7: Deploy Configuration File

Place the configuration file in the standard Kubernetes location:

### Create the .kube directory if it doesn't exist

mkdir -p ~/.kube

### Copy the config file to the standard location

cp ~/config ~/.kube/config

### Set appropriate permissions (security best practice)

chmod 600 ~/.kube/config

What this accomplishes: Kubectl will automatically find and use the configuration file in this standard location.


Step 8: Test and Authenticate Your Access

Now test that everything is working correctly:

Run the test command:

kubectl -n <namespace> get pods


Expected first-time behavior: You'll see a message like:Please visit the following URL in your browser: https://authentik.nrp-nautilus.io/device?code=XXXXXXXX