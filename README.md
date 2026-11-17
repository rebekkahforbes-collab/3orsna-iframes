# 3orsna — iframes

Every 3orsna iframe, published with GitHub Pages. Each Wix HTML element points at its file here (**Website address**), so updating an iframe is just a commit. No pasting into Wix.

This repository must stay **public** (GitHub Pages is free for public repositories). Nothing secret lives here: it's the same code any visitor's browser already downloads.

| Wix page | HTML element | Website address |
|---|---|---|
| Custom Signup | `#signupFrame` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/signup.html` |
| MY WEDDING | `#dashFrame` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/couple-dashboard.html` |
| EDIT WEDDING | `#builderFrame` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/wedding-builder.html` |
| MY GUESTS | `#guestsFrame` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/guest-list.html` |
| Weddings (Item) | `#inviteFrame` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/wedding-invite.html` |
| VENDOR DASHBOARD | `#html1` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/vendor-dashboard.html` |
| ADD LISTING | `#addFrame` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/vendor-add.html` |
| VENUES | `#html1` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/venues.html` |
| VENUES (Item) | `#html1` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/venue-detail.html` |
| TALENT DASHBOARD | `#html1` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/talent-dashboard.html` |
| Talent Edit (Item) | `#html1` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/talent-edit.html` |
| WEDDING TALENT | `#html1` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/talent-directory.html` |
| Talent (Item) | `#html1` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/talent-profile.html` |
| Admin Dashboard | `#adminFrame` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/admin-dashboard.html` |
| HOME | `#latestFrame` | `https://rebekkahforbes-collab.github.io/3orsna-iframes/home-latest.html` |

After a commit, GitHub Pages takes a minute or two to publish, and browsers may cache the old file for up to 10 minutes. Hard-refresh (Ctrl/Cmd + Shift + R) to see the change sooner.

`tools/build-invite.py` rebuilds `wedding-invite.html` from `wedding-builder.html`. Run it only after changing the builder's designs (`python3 tools/build-invite.py`); never edit `wedding-invite.html` by hand.
