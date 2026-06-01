# Remotion Video App Rules

This repo (`miasstack/ai-studio`) is a Remotion-based video app using React.
Docs: https://www.remotion.dev/docs/

## Project Structure

Root file: `src/Root.tsx`
```tsx
import {Composition} from 'remotion';
export const Root: React.FC = () => (
  <>
    <Composition
      id="MyComp"
      component={MyComp}
      durationInFrames={120}
      width={1920}
      height={1080}
      fps={30}
      defaultProps={{}}
    />
  </>
);
```

**Defaults:** 1920×1080, 30fps, id="MyComp"

## Core Hooks
- `useCurrentFrame()` — current frame number (starts at 0)
- `useVideoConfig()` — get `{fps, durationInFrames, height, width}`

## Special Tags (use these instead of native HTML)
- `<OffthreadVideo>` — for video (not `<video>`)
- `<Img>` — for static images
- `<Audio>` — for audio
- `<AbsoluteFill>` — layering elements on top of each other
- `<Sequence from={n} durationInFrames={n}>` — timing elements
- `<Series>` / `<Series.Sequence durationInFrames={n}>` — elements in sequence
- `<TransitionSeries>` with `<TransitionSeries.Transition>` — transitions between sequences

## Static Assets
```tsx
import {staticFile} from 'remotion';
<Audio src={staticFile('audio.mp3')} />
```

## Animation Utilities
```tsx
import {interpolate, spring, random} from 'remotion';

// Interpolate (always add clamp extrapolation)
const value = interpolate(frame, [0, 100], [0, 1], {
  extrapolateLeft: 'clamp',
  extrapolateRight: 'clamp',
});

// Spring animation
const value = spring({ fps, frame, config: { damping: 200 } });

// Random (NEVER use Math.random())
const value = random('my-seed'); // returns 0-1
```

## Critical Rules
1. **NEVER use `Math.random()`** — use `random('seed')` from remotion
2. **No user interactions** — no onClick, onHover, useState for interactivity
3. **No useEffect** — calculations must be pure, based on frame number
4. **Deterministic only** — same frame always produces same output
5. Animations are driven by **frame number**, not time or events
6. All props must be passed at **composition time** via defaultProps

## Remotion vs Normal React

| Remotion | Normal React |
|----------|-------------|
| `useCurrentFrame()` for state | `useState()` for state |
| `interpolate()` / `spring()` for animation | CSS transitions / requestAnimationFrame |
| No user input | Handles clicks, forms, gestures |
| No `useEffect` | `useEffect` for side effects |
| Pure, deterministic | Can have side effects |

## GIF Support
```tsx
import {Gif} from '@remotion/gif';  // install @remotion/gif first
<Gif src="https://..." style={{width: '100%'}} />
```

## Transitions
```tsx
import {linearTiming, springTiming, TransitionSeries} from '@remotion/transitions';
import {fade} from '@remotion/transitions/fade';
import {wipe} from '@remotion/transitions/wipe';
// TransitionSeries.Transition must be between TransitionSeries.Sequence tags
```

## Sequence Timing Notes
- `Sequence from={10}` — appears after frame 10
- `from` can be negative — starts immediately but cuts off first N frames
- Child components' `useCurrentFrame()` resets to 0 at the start of their Sequence
- `Series.Sequence` has `offset` prop (not `from`)
- `TransitionSeries.Sequence` has neither `from` nor `offset`
