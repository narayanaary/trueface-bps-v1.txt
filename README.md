# TrueFace BPS // Bypass Protocol System

TrueFace BPS is an ultra-lightweight, asynchronous JavaScript wrapper engineered to interface seamlessly with client-side verification environments. It normalizes data streams and frames in real-time to eliminate infinite biometric failure loops and minimize user-facing friction.

## Core Features
- **Stream Normalization:** Minimizes client-side exposure and lighting errors.
- **Asynchronous Execution:** Lightweight footprint (<12KB) with zero dependencies.
- **Event-Driven Hooks:** Exposes clean event handlers (`onHook`, `onSuccess`).

## Basic Implementation

Deploy the primary script wrapper within your application's header before initialization:

```html
<!-- Initialize TrueFace BPS Engine -->
<script src="trueface-bps-v1.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    TrueFaceBPS.initialize({
      environment: "production",
      recoveryMode: true,
      autoCalibrate: true,
      maxAttemptsBeforeBypass: 2
    });
  });
</script>
