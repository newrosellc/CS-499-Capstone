---
layout: default
title: Algorithms and Data Structures Enhancement
---

# Algorithms and Data Structures Enhancement

## Artifact

OpenGL 3D Scene Rendering Project

## Enhancement Summary

The rendering system was redesigned using texture batching and hash-based lookups.

## Improvements

- Replaced linear texture searches with unordered_map lookups.
- Reduced texture binding operations.
- Improved rendering efficiency.

## Complexity Analysis

Previous approach:
- Texture lookup O(n)

Enhanced approach:
- Texture lookup O(1)

This reduced overall rendering overhead because lookups occur during every render pass.
