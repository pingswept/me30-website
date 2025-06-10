---
title: "Class 07: Low power/high power"
draft: false
---

## Controlling high power with low power

## Electromechanical relays

Before transistors, and still in some cases today, we used electromechanical relays to control large currents. The basic idea of a relay is that you've got a little coil of wire in a tiny box. You run a small current through the wire, which makes a magnetic field, which pulls a little metal lever, closing a circuit that can handle a lot of current.

![An electromechanical relay](/img/relay.png)

Relays have a few major advantages.
* You can hear and see them open and close. (Usually, they're in a clear plastic box.)
* They are simple to understand.
* They can provide isolation between a high voltage circuit and a low voltage circuit. (A relay used for this purpose, like in a golf cart, is called a contactor.)

Everything else about them is terrible.

* They're slow.
* They're relatively unreliable.
* They're expensive to make.
* They're big.
* They require a relatively large current to operate.
* If you badly overload them, they weld shut.

In general, you probably shouldn't use relays unless you need a safety circuit that pops open when the power fails, like in a table saw, or somebody gives you a pile of relays for free.

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_zjs0ytpn&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_3ybyae4m" width="736" height="450" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

## The new hotness: transistors

There's a huge amount to learn about transistors; the topic can be overwhelming. First, let's narrow things down to just two common varieties of transistor and explain two ways each can be used.

![2 transistors](/img/transistors.jpg)

## Bipolar junction transistor (BJT)

If someone just says "transistor" to you, they probably mean a bipolar junction transistor, or BJT. If someone mentions an NPN or PNP transistor, they are also talking about BJT's.

The fundamental characteristic of a BJT is that it is a **current-controlled device**: putting a small amount of current through one leg of the device allows a larger current to flow through another leg of the device.

![Typical BJT circuit](/img/typical-bjt-circuit.jpg)

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_si4itzhx&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_e7j05ntn" width="736" height="450" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

## Metal oxide semiconductor field effect transistor (MOSFET)

MOSFETs are a newer variety of transistor than BJTs. If someone mentions an N-channel or P-channel device, they're usually talking about a MOSFET.

The fundamental characteristic of a MOSFET is that it's a **voltage-controlled device**: raising the voltage on one leg of the device (the gate) reduces the resistance between two other legs of the device (the drain and source).

![Typical MOSFET circuit](/img/typical-mosfet-circuit.png)

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_7yav5me2&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_k5di3h4b" width="736" height="450" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

## Two ways to use a transistor

There are two major ways that a transistor can be used: as an **amplifier** or a **switch**. In digital electronics, which has largely superseded analog electronics over the last few decades, we largely use transistors as switches rather than amplifiers.

(It should be noted here that because physical phenomena are, in reality, analog in nature, at the lowest levels, electronics will always be analog. But, for everyday engineering tasks, you will largely encounter digital devices. If the analog stuff is interesting to you, dive into it; a deeper understanding of analog stuff can only benefit you.)

### 27P06 P-channel MOSFET ###

So close ...

![So close](/img/27pp06-license-plate.jpg)
