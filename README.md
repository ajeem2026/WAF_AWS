# WAF_AWS

As outlined in the diagram, the user request will point to a web app (simple HTML code) and this webApp will point to Route53 which will point to CloudFront. 

What is Route53?
=> A scalable DNS and Domain Name Registration service. It also allows you to create endpoints so you can route users to certain applications if they hit a certain endpoint.  

The reason I am using cloudFront is because I want to have https with caching. In order to use CloudFront, I need an Amazon Certificate Manager (ACM). Finally, I will use Amazon S3 to upload my index.html file. 

0312

My static website is now hosted on Amazon S3— that's my work done with AmazonS3 and Route53. Now the issue is security. In order to make website secure, I am going to use CloudFront and to use CloudFront, I will need to configure its ACM. 

Firstly, I went to Certificate Manager in AWS and requested a public certificate for my website using the default DNS validation method and RSA 2048 encryption algorithm. 

Secondly, after my certificate is validated, I need to create records in Route53 with just clicking a button in the ACM interface. Now, going back to my hosted zone in Route53, I can see that I have two more records added with the type "CNAME". 

Thirdly, I am now going to CloudFront after my successful cert validation and creation of the two records. After going to cloudfront, I am first creating a cloudFront distribution. Here, I first have to copy the origin domain. For which I go back to S3 and select the bucket with "www" version --> properties --> copy the link from "Static Website Hosting" section under the label "Bucket Wesbite Endpoint" at the very bottom. Paste this link into CloudFront and keep all the default configurations. The only change:

In Viewer protocol policy, change it to : "Redirect HTTP to HTTPS". Again within "Custom SSL certificate" --> choose the certificate that you just created. Also, in Alternative DOmain name (CNAME) put in the "www" version of your static website. 
