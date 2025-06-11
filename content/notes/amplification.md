---
title: "Class 22: Sensor amplification"
draft: false
---
## Sensor amplification

Sensors produce real small voltages, so we need to amplify them.

![server-client architecture options](/img/client-server-table.jpg)

{{< katex display >}}
V_{in} = V_{out} * \frac{R_1}{(R_1 + R_2)}

\frac{V_{in}}{V_{out}} = \frac{R_1}{(R_1 + R_2)}

Gain = \frac{V_{out}}{V_{in}} = \frac{(R_1 + R_2)}{R_1}

Gain = 1 + \frac{R_2}{R_1}
{{< /katex >}}
