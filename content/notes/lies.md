---
title: "Lies we tell you"
draft: false
---

## Lies we tell you

When we talk about electricity and magnetism, we use a lot of metaphors about water and gestures about imaginary field lines in loops. Mostly, the metaphors and such help you understand how electricity works, and, of course, you know electricity isn't *really* the same as water.

However, maybe it's useful to note a few things that we know are true that conflict with the little stories we tell you.

## The big one

The big difference between what we tell you and the truth is that we have the polarity of electron flow wrong. We pretend that current flows from the positive terminal of a battery through a circuit to the negative terminal. In truth, the charged particles, electrons, are moving in the other direction. You know all those diodes you used to block current in one direction-- they were actually blocking current in the other direction. This is why the weird names "source" and "drain" MOSFETs have for their terminals are backwards-- electrons are really flowing from source to drain, like any sensible person would expect.

("WHY! Why does it have to be like this?" you yell at the sky late at night. I don't know. Historically, it has something to do with physicists and engineers not being good at listening to each other.)

## How fast electrons move

Electrons move **extremely** fast. In a copper conductor, they move at around 1,000,000 m/s, and electric fields propagate even faster, at about half the speed of light. But, as electrons move through a metal like copper, they crash into each other constantly, trillions of times per second. So, even though they're moving fast, they're going in the direction that the electric field is pushing them only a little more than half the time. The speed at which an electron's average position in a conductor changes is actually surprisingly slow-- more like 1 mm/s. For AC, where the polarity of the voltage is changing 50 or 60 times per second, electrons are staying in basically the same place, on average. Each individual electron is moving fast, but crashing into another electron every 10 nm or so, so they don't make it very far in any one direction.

If you want to know more about this, you could google "drift velocity" and "mean free path."

Also, for what it's worth, you could keep believing these lies, and you'd do a fine job as an engineer, as long as you weren't the one designing the guts of integrated circuits.


