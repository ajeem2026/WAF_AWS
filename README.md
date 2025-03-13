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

In Viewer protocol policy, change it to : "Redirect HTTP to HTTPS". Again within "Custom SSL certificate" --> choose the certificate that you just created. Also, in Alternative DOmain name (CNAME) put in the "www" version of your static website. Finally, enable AWS WAF for security implementation and create distribution. 

Now that we have a distrubtion for the "www" version of my website, I am now going to create another distribution for the non-www version using the same procedure. Now I have my 2 distributions ready. 

Final two things now: Our distribution is NOT secure without HTTPS and the MAIN domain name is still in the "code".cloudfront.net format (this can be accessed now without the HTTPS warning tho). We have to make final two configurations to ensure this is fixed. 

I am going back to S3 to my buckets and under "Properties" I am going to edit "Static Website Hosting" protocol from HTTP to HTTPS. 

To change the main domain name, we go back to Route53 and find the two records with CNAME type. First, we will check the record with "A" type and then edit record. Here, we need to change "Route traffic to" from Alias to S3 website endpoint to "Alias to Cloudfront distribution." and then we choose the our distribution which will already be provided by the system. 

Now do the same changes for the other type A record (which will hold the "www." version). You will notice that the system automatically gives you the distribution domain name. 

That's it! Now I've successfully deployed my first static website using AWS.
