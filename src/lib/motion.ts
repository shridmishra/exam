/**
 * Shared Motion spring configurations for ultra-smooth layout animations.
 * Calibrated for instant responsiveness and natural momentum.
 */

export const tabSpringTransition = {
  type: "spring" as const,
  stiffness: 380,
  damping: 30,
  mass: 0.75,
};

export const filterSpringTransition = {
  type: "spring" as const,
  stiffness: 420,
  damping: 32,
  mass: 0.7,
};
