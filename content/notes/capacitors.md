---
title: "Class 03: Capacitors"
draft: false
---

## Physical description

All capacitors are thin plates of conductive material separated by a thin layer of insulating material. For the cylindrical electrolytic capacitors in your kit, they are made of two narrow strips of metal foil separated by a strip of thin brown paper, rolled up like a cinnamon roll.

## Farads

Capacitors are measured in farads. 1 F is 1 coulomb/volt, a measure of how much charge it takes to raise the voltage of the capacitor by 1 volt. Oddly, most of the capacitors we use in electronics are small relative to 1 F, usually in the range of microfarads (uF, 10^-6) down to picofarads (pF, 10^-12).

## Voltage-current relationship

Capacitors behave like frequency-dependent resistors. The governing equation is: {{< katex >}}I = C dV/dt{{< /katex >}}, where {{< katex >}}I{{< /katex >}} is current, {{< katex >}}C{{< /katex >}} is capacitance, and {{< katex >}}dV/dt{{< /katex >}} is the rate at which the voltage is changing. The capacitance is a physical property of a capacitor, and is more or less constant. When the frequency of a signal is high, {{< katex >}}dV/dt{{< /katex >}} is high, so more current flows. This makes the apparent resistance of capacitor low at high frequency. The reverse is also true: a capacitor appears high resistance to low frequency signals.

## But what is the point of them?

Capacitors can be used in two main ways: as a small battery and as a filter.

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_0oysx6kc&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_1u6i4tk6" width="736" height="450" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1813261/sp/181326100/embedIframeJs/uiconf_id/26203331/partner_id/1813261?iframeembed=true&playerId=kaltura_player&entry_id=1_3053wks8&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_ireo6qoe" width="736" height="450" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

## The time-dependent behavior of a capacitor acting like a small battery in an R-C circuit

Consider the circuit below. 

![Classic charge-discharge R-C circuit with LED](/img/Capacitor_RC_Schematic.jpg)

Both buttons are initially open. We can charge up the capacitor by pressing only the "charge" button for a moment. The voltage across the capacitor and the current through it will behave as shown in these curves.

![Capacitor charging V-t and I-t curves](/img/Capacitor_Charging_Curves.jpg)

Then, let go of the "charge" button, and press and hold down the "discharge" button. You'd get the following voltage and current dynamics. And the dwindling current would be evident in the fading of the LED.

![Capacitor discharging V-t and I-t curves](/img/Capacitor_Discharging_Curves.jpg)

We can model the discharge rate of the capacitor, which also tells us the fading rate of the LED.  In the math below, we treat the combined resistance of the resistor and LED as just "R."

![Creating and solving the differential equation for an R-C circuit](/img/Capacitor_Discharging_Math.jpg)


