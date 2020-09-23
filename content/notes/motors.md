---
title: "Motors"
draft: false
---

## Common characteristics

There are a few characteristics that virtually all motors share. Let's go over those first; then we can discuss different variants.

First off, every motor has a part that spins, called the **rotor** and a part that stands still, called the **stator**. Usually, the rotor is in the middle of the motor, and the stator is around the outside, but there are also motors called "outrunners" where the outside rotates and the stator is fixed inside.

Power is the product of torque and speed, so for a given power level, to get more torque, you need to slow down. But, the efficiency of motors tends to drop with speed, so it's usually wiser to run a motor at a high speed and then use a gearbox to drop the speed and increase the torque. You do lose a little energy to friction in the gearbox, but less than you would lose with a slower motor.

Usually, the limits of motor performance are thermal; if you drive too much current through a motor, the wire inside will get hot enough that its insulation will melt, which will create a short circuit. Then, lots of current will flow, and your motor will be destroyed. In general, the maximum torque you can get out of the motor before the insulation melts is roughly proportional to the volume of the motor. There are lots of different geometries-- long, thin motors and short, wide motors-- but if the volume is similar, the torque is similar.

## Fundamental principle

The fundamental principle of a motor is to run some electric current in a wire that is perpendicular to a magnetic field, which generates a force on the wire. If the wire is attached to a shaft mounted on bearings, that force acts as a torque, which spins the shaft.

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_45k3qkx7&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_t9h074m7" width="736" height="450" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

## Motor types

There are many kinds of motors, but let's start with the three types in your project kits:

1. a brushed DC gearmotor
2. a NEMA 17 stepper motor
3. a hobby servo

First off, let's expose a lie: the hobby servo is, in fact, a brushed DC motor hidden inside a plastic box, so the truth is that you only have two kinds of motors. The box also contains a geartrain, a motor controller IC, an H-bridge and a potentiometer.

![stepper motor](/img/stepper-motor.jpg)
![stepper motor guts](/img/stepper-motor-guts.jpg)
![stepper motor rotor](/img/stepper-motor-rotor.jpg)
![hobby servo](/img/hobby-servo.jpg)
![hobby servo guts](/img/hobby-servo-guts.jpg)
![hobby servo h-bridge](/img/hobby-servo-h-bridge.jpg)

The H-bridge in the servo uses two Rohm 2SD2118 NPN power transistors and two complementary 2SB1412 PNP transistors.

On the underside of the PCB is a Hitec HT7003 analog controller.
