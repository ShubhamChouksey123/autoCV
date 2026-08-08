# Shubham Chouksey

- **Role:** Senior Software Engineer at [New Relic](https://www.newrelic.com/) (Hyderabad, India) — promoted May 2026 (Software Engineer 2, August 2024 - May 2026)
- **Email:** shubhamchouksey1998@gmail.com
- **GitHub:** [ShubhamChouksey123](https://github.com/ShubhamChouksey123)
- **LinkedIn:** [contact-shubham-chouksey](https://www.linkedin.com/in/contact-shubham-chouksey/)
- **Portfolio:** [shubhamchouksey123.github.io/portfolio](https://shubhamchouksey123.github.io/portfolio/)
- **Education:** B.Tech, Indian Institute of Technology (IIT), Patna (2017 - 2021)

## Work Experience

This matches the trimmed bullets in `cv.tex` (kept in sync — update both together). The full, untrimmed detail this was distilled from lives in the FY26 performance review material (see Notes below) if more context is ever needed.

### Senior Software Engineer — New Relic (May 2026 - present)

- Promoted to Senior Software Engineer for technical leadership and reliability engineering; continuing to own the Secrets Store platform with expanding architecture scope.

### Software Engineer 2 — New Relic (August 2024 - May 2026)

- Built and owned the Secrets Store platform (three-layered encryption, 30K RPM throughput, high availability, low latency) and led its real-time CDC pipeline (Kafka, Flink, PostgreSQL logical replication) for event-driven secret propagation to downstream consumers.
- Built internal REST APIs and customer-facing GraphQL APIs for the Secrets Store, holding a 99.99% SLA across availability, latency, and error rate.
- Designed a Signing and Verification platform from scratch: key generation/rotation APIs, JWKS distribution via AWS S3 and Cloudflare CDN, and audit logging, with >90% test coverage.
- Built and maintained most of the Secrets Store infrastructure as Terraform-managed IaC — database, S3 buckets, AWS KMS keys, and New Relic alerts/service levels.
- Maintained 100% on-call availability and zero Sev 1-3 incidents across 197 merged PRs (82.8% merge rate); resolved a recurring connection-pool-exhaustion incident.
- Reviewed 200+ pull requests (~45% of the team's total), mentoring engineers on code quality, architecture, and observability.

### Associate Team Lead — Cognam (June 2023 - July 2024)

- Led design and development of a blockchain-based backend driving over $1 billion in monthly revenue for a leading international payment processor.
- Managed a 6-member back-end team — sprint planning, task allocation, and stakeholder management in an agile/scrum setup.

### Software Engineer — Cognam (June 2021 - May 2023)

- Delivered 30+ scalable APIs for a bank's enterprise mobile app: registration, login, profile updates, money transfers, and notifications.
- Built a block-reader system syncing a database with blockchain at up to 100,000 transactions/sec, adding decentralized capability to traditional banking systems.
- Automated ML-powered KYC on the Issuer Server, cutting manual work by 95%.

## CV variants

- `cv.tex` — primary resume, published by CI as the default (`make`).
- `cv-long.tex` — expanded/verbose variant with the same structure; build with `make NAME=cv-long`.

## Keyword shortlist for cv.tex (ATS / recruiter screening at product companies)

Candidate keywords for the Skills section (and, where relevant, Work Experience bullets) in `cv.tex`, aimed at ATS/recruiter screening at product-based companies (Google, Salesforce, Meta, Amazon, Microsoft-style bars). Checked items (`[x]`) are already present in `cv.tex` today; unchecked are candidates to shortlist. Mark the ones you want added, and note any that aren't actually true of your experience — don't add a keyword you can't back up in an interview.

### Languages
- [x] Java
- [x] Python
- [x] JavaScript
- [x] SQL
- [x] C/C++
- [ ] TypeScript
- [ ] Go
- [ ] Kotlin

### System design & architecture
- [x] System Design — in "Some More Skills"
- [x] Distributed Systems — in "Some More Skills"
- [ ] Scalability
- [x] High Availability — in "Some More Skills" and Work Experience bullet
- [x] Low Latency — "low latency" in Work Experience bullet (Skills list still says "High Availability" only, not "Low Latency" itself)
- [ ] Fault Tolerance
- [ ] Concurrency / Multithreading
- [x] Event-Driven Architecture — "event-driven secret propagation" in Work Experience bullet
- [ ] Caching (Redis/Memcached)
- [ ] Load Balancing
- [ ] Rate Limiting
- [ ] Idempotency
- [ ] Data Modeling
- [ ] Database Sharding / Partitioning
- [ ] Object-Oriented Design (OOD)
- [x] Design Patterns
- [x] Microservices

### Cloud & infrastructure
- [x] AWS
- [x] GCP
- [ ] Azure
- [ ] Kubernetes
- [x] Docker
- [x] Terraform — in Skills ("Technologies \& Tools") and Work Experience bullet
- [x] Infrastructure as Code (IaC) — "provisioned via Terraform" in Work Experience bullet
- [ ] Serverless / Lambda
- [ ] Service Mesh

### APIs, data & messaging
- [x] RESTful APIs — in Skills ("Technologies \& Tools") and Work Experience bullet
- [x] GraphQL — in Skills and Work Experience bullet
- [ ] gRPC
- [ ] Protocol Buffers
- [x] Kafka
- [ ] Event Streaming
- [x] Change Data Capture (CDC) — "CDC" in Work Experience bullet (not yet in Skills)

### Databases
- [x] MySQL
- [x] PostgreSQL — "PostgreSQL" appears in the Work Experience bullet, though the Skills row still says "Postgres"
- [x] MongoDB
- [ ] Redis
- [ ] DynamoDB
- [ ] Elasticsearch
- [ ] Database Indexing / Query Optimization

### Security
- [ ] OAuth2 / OIDC
- [ ] JWT
- [x] Encryption (AES/RSA) — "three-layered encryption" in Work Experience bullet (AES/RSA not spelled out)
- [x] Key Management (KMS) — "AWS KMS" in Work Experience bullet
- [ ] IAM
- [ ] Zero Trust

### Reliability & observability (SRE-flavored — strong fit given on-call/reliability content already in Work Experience)
- [x] Site Reliability Engineering (SRE) — in "Some More Skills"
- [x] SLA / SLO / SLI — "99.99\% SLA" in Work Experience bullet (SLO/SLI not separately mentioned)
- [x] Observability — in Work Experience bullet
- [ ] Monitoring & Alerting
- [ ] Incident Management
- [ ] Postmortems / Root Cause Analysis (RCA)
- [x] CI/CD

### Testing & quality
- [x] JUnit
- [x] Unit Testing
- [ ] Integration Testing
- [ ] Test-Driven Development (TDD)
- [ ] Mocking (Mockito)
- [ ] Static Analysis

### Practices & collaboration
- [x] Agile / Scrum — "agile/scrum" in Cognam Work Experience bullet
- [ ] Technical Design Docs / RFCs
- [x] Code Review — "Reviewed 200+ pull requests" in Work Experience bullet
- [x] Mentorship — "mentoring engineers" in Work Experience bullet
- [ ] Cross-functional Collaboration

## Notes

Source of truth for work history is the FY26 performance review material
(`/Users/schouksey/Documents/work/learn/performance-review`) — pull from there when
updating the New Relic bullets in `cv.tex`, and sanitize out internal-only details
(Jira/DACI ticket IDs, internal PR links, internal tool names) before adding to the CV.
