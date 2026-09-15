import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the top gradient (TOC -> Yapsu AI)
# Replace the old dark gradient with a soft off-white gradient
old_top_grad = r'<div className="absolute top-0 left-0 w-full h-\[250px\] bg-gradient-to-b from-\[#0a0a0a\].*?</div>'
new_top_grad = '<div className="absolute top-0 left-0 w-full h-[250px] bg-gradient-to-b from-[#F4F1EA] to-[#FCFBF9] z-10 pointer-events-none"></div>'
content = re.sub(old_top_grad, new_top_grad, content, flags=re.DOTALL)

# 2. Fix the bottom gradient (Yapsu AI -> Chinese Debate)
# Instead of an absolute gradient at the bottom of Yapsu, we will append a bridging section
old_bottom_grad = r'<div className="absolute bottom-0 left-0 w-full h-\[400px\] bg-gradient-to-b from-transparent to-\[#06112E\].*?</div>'
content = re.sub(old_bottom_grad, '', content, flags=re.DOTALL)

# Add the bridging gradient section right after </section> of yapsu-ai
bridge_section = """
        {/* Smooth Transition to Chinese Debate 2026 */}
        <div className="w-full h-[300px] bg-gradient-to-b from-[#FCFBF9] to-[#06112E]"></div>
        
        {/* Skeleton for Chinese Debate 2026 to ensure the gradient blends perfectly */}
        <section id="chinese-debate-2026" className="relative w-full py-20 bg-[#06112E] text-white">
            <div className="max-w-[1400px] mx-auto px-6 text-center">
                <h2 className="font-['Fredoka'] text-[60px] font-bold text-cyan-400 drop-shadow-[0_0_15px_rgba(34,211,238,0.6)]">
                    02. Chinese Debate 2026
                </h2>
            </div>
        </section>
"""
if '<section id="chinese-debate-2026"' not in content:
    content = content.replace('</section>\n\n        {/* Add more sections here later */}', '</section>\n' + bridge_section + '\n        {/* Add more sections here later */}')
    content = content.replace('</section>\n      </main>', '</section>\n' + bridge_section + '\n      </main>')

# 3. Replace the 16 frames in the Experience Flow (Flat Grid)
old_grid_pattern = r'\{\[\s*// ---------------- ROW 1 ----------------.*?\]\.map'
new_grid = """{[
                       // ---------------- ROW 1: ONBOARDING & ROADMAP ----------------
                       // ONBOARDING (Personalize, Permissions, Aha Moment, Demo/Sign In)
                       "final_screens/01_onboard_personalize.jpg",
                       "final_screens/02_onboard_permissions.jpg",
                       "final_screens/03_onboard_aha.jpg",
                       "final_screens/04_onboard_signin.jpg",
                       
                       // ROADMAP (Map of lessons, Vocab/Grammar Check)
                       "final_screens/05_roadmap_map.jpg",
                       "final_screens/06_roadmap_progress.jpg",
                       "final_screens/07_roadmap_vocab.jpg",
                       "final_screens/08_roadmap_grammar.jpg",
                       
                       // ---------------- ROW 2: DRILL & ROLEPLAY ----------------
                       // DRILL (Fill in the blank, Matching, Repeat after)
                       "final_screens/09_drill_fill.jpg",
                       "final_screens/10_drill_matching.jpg",
                       "final_screens/11_drill_repeat.jpg",
                       "final_screens/12_drill_amazing.jpg",
                       
                       // ROLEPLAY (Gradient BG, Hint/Correction, Feedback, Transcript)
                       "final_screens/13_roleplay_gradient.jpg",
                       "final_screens/14_roleplay_hint.jpg",
                       "final_screens/15_roleplay_feedback.jpg",
                       "final_screens/16_roleplay_transcript.jpg"
                    ].map"""
content = re.sub(old_grid_pattern, new_grid, content, flags=re.DOTALL)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
