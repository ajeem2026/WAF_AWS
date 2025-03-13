# WAF_AWS

What is AWS WAF? AWS's own web application firewall. It is a managed WAF service that integrates natively with many resources running in AWS and gives us control over HTTPS requests. We can set custom rulesets without having to download any external software. 

We can use AWS WAF to protect our resources like:

1. Application load balancers (ALBs)
2. Amazon CloudFront Distributions (Amazon's CDN service)
3. Amazon API Gateway APIs (their API management service)
4. AWS AppSync GraphQL APIs (graphQL service)
5. Amazon Cognito User pools (customer identity and access management service)
6. Amazon ECS containers (Elastic Container Service)


WAF works on 3 different components:

1. Web Access Control Lists (ACLs) which are made up of rules
2. Rules: Statements that define inspection criteria and the action to take if web request matches the criteria
3. Rule groups: Reuasble groups of rules (there are internal ones and custom ones we can make ourselves!)



Section-1: Creating a web ACL

1.  
