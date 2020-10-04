---
title: "The Internet"
draft: false
---

## The Internet: how does it work?

Suppose you're sitting in your apartment, watching some crazy person on Zoom tell you about this new website about electronics that everybody is talking about. She says that the name of the website is [andnowforelectronics.com](http://andnowforelectronics.com), and she pastes a link to the site into the chat window. What happens when you click on the link?

## First, name resolution

First, your computer sends a universal datagram packet (UDP) to port 53 on a domain name system (DNS) server somewhere on the internet. The job of a DNS server is to look up the IP address of the website you're looking for in the distributed global database of domain names.

If you have wireless where you live, the server that your computer targets is probably your wireless router. If you're using your phone, it's a server that's run by AT&T, Verizon, or some phone company like that, and your phone was told where to find it when it connected to the cellular network. You could also be using a public server; for example, Google runs two public DNS servers at the weird IP addresses 8.8.8.8 and 8.8.4.4.

So your computer sends off the UDP packet saying, "Hey, where can I find [andnowforelectronics.com](http://andnowforelectronics.com)?" Despite the site's worldwide popularity, your wireless router probably has no idea, so it makes a request like yours to the DNS server run by whoever sells you an internet connection, like RCN or Comcast.

But again, despite the site's worldwide popularity, Comcast has no idea where to find it, so it makes a request to the authoritative name server for all the domain names that end in .com. If Comcast's server didn't know where to find that server, it could ask one of the 13 root name servers; those servers' addresses are hard-coded into the Comcast server's memory, but Comcast has seen bajillions of requests for .com addresses before, so it surely has the .com name server address cached.

Finally, the .com server sends Comcast over to the authoritative server for andnowforelectronics.com, which is a server run by a domain name registrar in Paris, France, called gandi.net. Their name server, ns1.gandi.net, at long last, answers the question! They do this because I pay them to, and they know the right IP address because I typed it into their website last summer.

Here's what their server sends back:

    id 65452
    opcode QUERY
    rcode NOERROR
    flags QR RD RA
    ;QUESTION
    andnowforelectronics.com. IN A
    ;ANSWER
    andnowforelectronics.com. 10799 IN A 23.239.11.134
    ;AUTHORITY
    ;ADDITIONAL

That IP address gets passed back to your web browser, and all the DNS servers along the way cache the answer, in case someone else wants to know where to find the site.

## Second, connect to the webserver

stuff about TCP/IP goes here

## Third, we ask the server for the webpage

stuff about HTTP, maybe HTTPS?

Should also add stuff about ports, NAT, and port forwarding
