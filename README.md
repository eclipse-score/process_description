# 📊 Eclipse S-CORE Process Description

## 🎯 **Overview**

The **Eclipse S-CORE Process Description** is a comprehensive process model designed to
establish organizational rules for developing **open source automotive software** in
**safety and security-critical contexts**.
This project is part of the Eclipse Foundation and provides standardized processes for
the automotive industry.


## 🚀 **Key Features & Purpose**

### **Primary Mission:**
- Establish organizational rules for automotive open source software development
- Enable safety and security compliance in automotive software projects
- Provide standardized processes for critical automotive applications

### **Standards Compliance:**

The process model conforms to state-of-the-art industry standards:

- **ASPICE PAM 4.0** (Automotive Software Process Improvement and Capability Determination)
- **ISO 26262** (Functional Safety for Road Vehicles)
- **ISO/SAE 21434** (Cybersecurity Engineering for Road Vehicles)
- **ISO PAS 8926** (Safety and Cybersecurity for Automated Driving Systems)


## 📋 **Core Process Areas**

The workspace is organized into comprehensive process areas:

### **🔧 Management Processes:**
- **Platform Management** - Project Management, Infrastructure and platform oversight
- **Safety Management** - ISO 26262 compliance, safety planning, anomaly handling
- **Security Management** - ISO/SAE 21434 compliance, security planning, vulnerability management
- **Quality Management** - ASPICE 4.0 compliance, quality assurance
- **Change Management** - Only way to contribute, Impact analysis for safety/security changes
- **Problem Resolution** - Issue tracking and resolution
- **Release Management** - Release planning and execution

### **🛠️ Development Processes:**
- **Requirements Engineering** - Requirements specification and traceability
- **Architecture** - Software architecture
- **Implementation** - Software development and coding
- **Verification** - Testing and verification processes
- **Safety Analysis** - Safety analysis
- **Security Analysis** - Security analysis

### **🎯 Support Processes:**
- **Configuration Management** - Version control and change tracking
- **Tool Management** - Development tool evaluation and qualification
- **Documentation Management** - Technical documentation processes


## 👥 **Roles & Responsibilities**

### **Key Roles Defined:**
- **Safety Manager** - Functional safety oversight and compliance
- **Security Manager** - Cybersecurity management and vulnerability handling
- **Quality Manager** - Quality assurance and process compliance
- **Project Lead** - Technical decision making and development coordination


## 🛠️ **Development Environment**

#### Run a documentation build:

```bash
bazel run //:docs
```

#### Access your documentation at:

- `_build/` for incremental
- `bazel-bin/bazel-bin/docs/_build/html`

#### Getting IDE support

Create the virtual environment via `bazel run //:ide_support`.\
If your IDE does not automatically ask you to activate the newly created environment you can activate it.

- In VSCode via `ctrl+p` => `Select Python Interpreter` then select `.venv_docs/bin/python` OR
- Click in the top level search bar, open `Show and Run Commands` => `Select Python Interpreter` then select `.venv_docs/bin/python`
- In the terminal via `source .venv_docs/bin/activate`

Now run the live_preview commands

```bash
bazel run //:live_preview
```

Now server should be available with a preview on the link that is given (normally 127.0.0.1:8000) and the documentation can be previewed there.

#### Explore more functions with
bazel query //...
