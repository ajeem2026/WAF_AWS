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

1. Search for AWS WAF service and click create web ACL
2.  I named my webACL and CloudWatch metric name "first_rules" and added my website as CloudFront Distribution resources.

Section -2: Creating rules:
1. Click on Add Rules and then select "Add managed rule groups" which gives us a list of pre-created rules. This is a list of managed rule groups from AWS and other organizations. In AWS paid rule groups, there are speciliased paid rules to prevent attack takeovers and fight against automated bots. For this project, we are going to use Free Rule Groups. 
2. Toggle "Add to web ACL" for the Amazon Reputation IP list and then minimize tab to "Add Rules"
3. The added rule will join our managed list of rules and now show to consume 25/5000 units of our WEBACL capacity

Section -3: Configuring rules
1. For the "Default web ACL action for requests that don't match any rules", we will allow the request to go through if it doesn't match any of the rules above.
2. Optionally, we can add a custom header to each request that was allowed to go through and AWS WAF will automatically prefix the custom header with x-amzn-waf-
3. If a bot is suspected, AWS WAF will verify the client with a captcha challenge. Once verified, we don't want to verify the client again when they travel to other parts of our application or domain. We can add those other app domains on our "Token Domain List"

Section-4: Setting rule priorities

1. This is important becasuse the first rules that match will be the ones that get evaluated.

Section-5: Configuring CloudWatch Metrics

What is CloudWatch? 
=> An AWS service that lets you observe and monitor your resources on AWS or on-premises. We get access to some free metrics as part of the free tier account. 

1. We keep these to the default configuration

Section-6: Review
1. Review settings and click on "Create web ACL" and we will make our WAF web ACL

Now we will access our Web ACL and notice that the screen displays useful information like requests per 5 minute period, sample requests and rules. 


On AWS WAF> Web ACLs > first-rules, click on the Rules tab,

1. Click on the name of the rules list that we set up earlier (Amazon Reputation IP list)
2. The AWS interface can be quite confusing as to what a particular rule actually does. For instance, in the "Rules in AWSManagedRulesAmazonIpReputationList" the action simply states "Use action defined in the rule." which is NOT helpful at all. However, researching the documentation of the rule can help us gain clarity on it. For IP reputation: https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html
3. Quick clarification on Count: Counts the request but does not block it (a passive approach). It continues to evaluate the rest of the rules. It also keeps track of how many times the request has been counted and inserts custom headers and adds labels for other rules. This is why RULE PRIORITES matter. If you have a higher rule priority that blocks a request before counting, we lose data on the count. In order to have it counted first before blocking, we have to set count to a higher priority rule in order for it get evaluated. 


This is the core of AWS WAF. Some other features are BOT control, Application Integration SDKs for addtional user telemetry and improved bot detection, IP sets, Regex pattern sets and our own rule groups, and specially Add-on protections that gives us access to the OWASP top 10 ruleset.






