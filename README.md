# a distributed system for my home network for creating visualizations with manim quickly.

# NetworkNodes: Distributed Computing Framework (Alpha)

## Overview
NetworkNodes is an experimental framework that aims to democratize distributed computing by making it accessible to anyone with multiple computers on a local network. Currently in alpha, this project provides a foundation for running distributed workloads across home networks and small clusters.

## 🌟 Vision
Our goal is to create a "plug-and-play" distributed computing environment that allows users to:
- Automatically discover and configure network resources
- Share memory and computational tasks across devices
- Distribute rendering and computational workloads
- Scale from 2 to N devices without complex configuration

## 🎯 Current Focus
The immediate roadmap focuses on supporting distributed [Manim](https://www.manim.community/) animations, allowing users to:
- Split animation rendering across multiple machines
- Share resources and assets efficiently
- Reduce rendering times for complex mathematical animations
- Combine rendered segments automatically

## ⚡ Current Features (Alpha)
- Automatic network device discovery
- Git repository initialization across nodes
- Basic shared memory implementation
- Automated node configuration
- SSH-based secure communication

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git installed on all nodes
- SSH access between machines
- Local network connectivity

### Required Python Packages
```bash
pip install paramiko netifaces shared_memory_dict gitpython
```

### Basic Usage
1. Clone this repository:
```bash
git clone https://github.com/yourusername/networknodes
cd networknodes
```

2. Configure SSH keys for all machines:
```bash
ssh-keygen -t rsa
ssh-copy-id user@machine1
# Repeat for all machines
```

3. Run the initialization script:
```bash
python setup_network.py
```

## 🏗️ Architecture
- Node Discovery: Automatic detection of compatible devices on local network
- Repository Management: Git-based configuration and code distribution
- Shared Memory: Cross-machine memory sharing for efficient data access
- Task Distribution: Fair distribution of computational workloads

## 🔄 Current Limitations
- Limited to local network environments
- Requires SSH key setup
- Basic shared memory implementation
- No fault tolerance yet
- No dynamic resource allocation

## 🛣️ Roadmap
- [ ] Implement Manim rendering distribution
- [ ] Add dynamic resource discovery
- [ ] Improve shared memory with Redis/memcached
- [ ] Add fault tolerance and recovery
- [ ] Create web-based monitoring interface
- [ ] Support dynamic node addition/removal
- [ ] Add workflow templating system

## 🤝 Contributing
This project is in alpha and actively seeking contributors! Areas where we need help:
- Distributed rendering optimizations
- Network protocol improvements
- Documentation
- Testing across different network configurations
- UI/UX for monitoring and control

## ⚠️ Warning
This is alpha software! Use at your own risk and expect breaking changes.

## 📜 License
MIT License - See LICENSE file for details

## 🙏 Acknowledgments
- Manim Community for inspiration
- Distributed Computing pioneers
- Open source community

## 🔗 Contact
- Submit issues via GitHub
- Join our Discord (coming soon)
- Follow development updates on Twitter (coming soon)

---

*NetworkNodes - Democratizing Distributed Computing, One Home Network at a Time*