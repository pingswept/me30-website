---
title: "The Internet"
draft: false
---

## The Internet: how does it work?

Suppose you're sitting in your apartment, watching some crazy person on Zoom tell you about this new website about electronics that everybody is talking about. She says that the name of the website is [andnowforelectronics.com](http://andnowforelectronics.com), and she pastes a link to the site into the chat window. What happens when you click on the link?

## First, name resolution

First, your computer sends a universal datagram packet (UDP) to port 53 on a domain name system (DNS) server somewhere on the internet. If you have wireless where you live, the server that your computer targets is probably your wireless router. If you're using your phone, it's a server that's run by AT&T, Verizon, or some phone company like that, and your phone was told where to find it when it connected to the cellular network. You could also be using a public server; for example, Google runs two at the weird IP addresses 8.8.8.8 and 8.8.4.4.

So your computer sends off the UDP packet saying, "Hey, where can I find [andnowforelectronics.com](http://andnowforelectronics.com)?" Despite the site's worldwide popularity, your wireless router probably has no idea, so it makes a request like yours to the DNS server run by whoever sells you an internet connection, like RCN or Comcast.

But again, despite the site's worldwide popularity, RCN and Comcast have no idea where to find it, so they make a request to the .com root server.
