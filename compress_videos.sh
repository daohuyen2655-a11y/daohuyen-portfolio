#!/bin/bash
set -e
echo "Compressing videos..."

cd public/assets/yapsu-ai/

# 1. Onboarding
mv "onboarding-feature.mp4" "onboarding-feature_orig.mp4"
ffmpeg -i "onboarding-feature_orig.mp4" -vcodec libx264 -crf 28 -vf "scale=-2:720" -preset veryfast "onboarding-feature.mp4"
rm "onboarding-feature_orig.mp4"
echo "Onboarding compressed."

# 2. Roleplay
mv "roleplay-feature.mp4" "roleplay-feature_orig.mp4"
ffmpeg -i "roleplay-feature_orig.mp4" -vcodec libx264 -crf 28 -vf "scale=-2:720" -preset veryfast "roleplay-feature.mp4"
rm "roleplay-feature_orig.mp4"
echo "Roleplay compressed."

# 3. Roadmap
mv "roadmap-drill-feature.mov" "roadmap-drill-feature_orig.mov"
ffmpeg -i "roadmap-drill-feature_orig.mov" -vcodec libx264 -crf 28 -vf "scale=-2:720" -preset veryfast "roadmap-drill-feature.mov"
rm "roadmap-drill-feature_orig.mov"
echo "Roadmap compressed."

echo "All done!"
