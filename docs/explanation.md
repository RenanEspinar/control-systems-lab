# Technical Explanation

## Why this project matters

Vacuum pressure control is important in biomedical and industrial systems where pressure must remain stable despite leakage, disturbances, or changes in system conditions.

This project compares two approaches:

- Open-loop control
- Closed-loop PID control

---

## Open-loop control

In open-loop control, the pump receives a fixed PWM signal.

The problem is that the system cannot correct itself if:

- leakage changes
- the chamber volume changes
- the pressure does not reach the desired value
- external disturbances appear

---

## Closed-loop PID control

PID control uses feedback from the pressure measurement.

The controller calculates the error:

e(t) = P_set - P(t)

Then it adjusts the pump command dynamically:

u(t) = Kp·e(t) + Ki∫e(t)dt + Kd·de(t)/dt

---

## Biomedical context

The pressure setpoint used in this model is:

-125 mmHg ≈ -16.7 kPa

This value is commonly used as a reference pressure in Negative Pressure Wound Therapy (NPWT).

---

## Engineering conclusion

The PID controller improves the system response by reducing steady-state error and allowing the pump to adapt to pressure changes.
