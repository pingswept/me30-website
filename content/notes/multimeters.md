---
title: "Class 02: Multimeters"
draft: false
---
## Multimeters

![NT8233D Pro multimeter](/img/nt8233d-pro-multimeter.jpg)

You might want to read the page on [series vs. parallel](/notes/series-vs-parallel/) connections before you read this one.

A modern digital multimeter has a whole bunch of different measurement tools packed into one box. The knob on the front allows you to pick which tool is active.

Generally, you can just crank the knob back and forth and try connecting the meter to different things, and nothing will really go wrong. **There is one exception: current measurement. If you connect the leads to the red port labeled "A" and then put the meter in series with a voltage source that can drive more than 10 A, you will burn out the 10 A fuse in the meter.** (That's what the little orange triangle and the label "FUSED 10A MAX" is trying to tell you. Blowing the fuse is not terrible, but then your meter won't be able to measure current until you replace the fuse, so don't do that.

## Voltage measurement

Voltage measurements are made by connecting the multimeter in parallel with the voltage you want to measure. The multimeter acts like a very high resistance. Inside the meter, the voltage charges up a small capacitor, and the amount of time it takes to charge the capacitor tells us how much voltage we're measuring. 

![measuring voltage](/img/measuring-voltage.png)

## Current measurement

![measuring current](/img/measuring-current.png)

## Resistance and continuity measurement

![measuring resistance](/img/measuring-resistance.png)

## What a multimeter looks like inside

![NT8233D Pro multimeter teardown overview](/img/neoteck-8233d-pro-teardown-overview.jpg)

![NT8233D Pro multimeter teardown pcb](/img/neoteck-8233d-pro-teardown-pcb.jpg)

![NT8233D Pro multimeter teardown knob](/img/neoteck-8233d-pro-teardown-knob.jpg)
