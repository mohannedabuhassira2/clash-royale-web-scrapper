import datetime

skipped_updates = {
    "On 3/5/2016, the May 2016 Update, increased the Common card level cap to 13 (from 12).",
    "On 3/5/2016, the May 2016 Update, increased the Rare card level cap to 11 (from 10).",
    "On 3/5/2016, the May 2016 Update, decreased the Legendary card level cap to 5 (from 6).",
    "On 3/5/2016, the May 2016 Update, changed the Dark Prince's card description. It used to say, \"Dealing area damage with each swing and double after charging, the Dark Prince is a formidable fighter. To harm his squishy core, break his shield first.\"",
    "On 3/5/2016, the May 2016 Update, changed the Golem's appearance to include crystals on its back and removed the team-colored spiked collars from its neck. However, the collar was reintroduced with the Elixir Golem.",
    "On 5/9/2018, the September 2018 Update, changed it so that Rare cards start at level 3 and end at level 13 (from 1 to 11).",
    "On 5/9/2018, the September 2018 Update, changed it so that Epic cards start at level 6 and end at level 13 (from 1 to 8).",
    "On 5/9/2018, the September 2018 Update, changed it so that Legendary cards start at level 9 and end at level 13 (from 1 to 5).",
    "On 2/9/2019, a Balance Update, fixed a bug where the Giant was incorrectly shown as a Melee: Long troop in his card info screen. He is now shown correctly as a Melee: Medium troop.",
    "On 15/4/2019, the April 2019 Update, added an extra Star Level.",
    "On 1/4/2021, there was a Troop Rush Challenge which spawned Skeletons with an invisibility mechanic like the Royal Ghost, except the Skeletons would never deactivate their invisibility, being unable to be directly targeted by enemy troops. The only way to defeat them was by using spell damage or if they were caught in area damage from an enemy troop.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Electro Spirit.",
    "On 26/11/2019, the End of November 2019 Update, removed the Freeze from Mega Deck Touchdown.",
    "On 26/11/2019, the End of November 2019 Update, removed the Freeze from Mega Deck Touchdown.",
    "On 7/6/21, the 2021 Quarter 2 Update slightly changed the Freeze's description, adding the phrase “Reduced damage to Crown Towers.” to it.",
    "On 19/9/2016, the September 2016 Update, changed the description slightly. It used to say: “A pair of unarmored ranged attackers. They'll help you with ground and air unit attacks, but you're on your own with coloring your hair.",
    "On 4/10/22, the Goblins were supposed to have 4 units instead of 3, but the change was pulled back last minute due to an issue that requires a client update to fix.",
    "On 30/9/2019, the End of September 2019 Update, added an extra Star Level.",
    "On 4/10/22, the Knight was supposed to get a 3% HP buff, but the change was pulled back last minute due to an issue that requires a client update to fix.",
    "On 20/1/2020, a maintenance break, added a card render to the Archers' card info screen.",
    "On 19/9/2016, the September 2016 Update, changed the description slightly. It used to say: “A pair of unarmored ranged attackers. They'll help you with ground and air unit attacks, but you're on your own with coloring your hair.",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Witch from Training Camp to Bone Pit (Arena 2).",
    "On 20/1/2020, a maintenance break, added a card render to the Witch's card info screen.",
    "On 7/6/2021, the 2021 Quarter 2 Update moved the Arena to unlock the Witch from Bone Pit (Arena 2) to Spell Valley (Arena 5).",
    "On 28/4/2022, a maintenance break changed the Witch's card image and card render.",
    "On 1/8/22, a maintenance break changed the Barbarians' card icon and card render, by making them look pixilated.",
    "On 2/9/22, a maintenance break reverted the Barbarians' card icon and card render to their state before 1/8/22.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Golem from Builder's Workshop (Arena 6) to Barbarian Bowl (Arena 3).",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Valkyrie from Goblin Stadium (Arena 1) to Bone Pit (Arena 2).",
    "On 7/6/21, the 2021 Quarter 2 Update changed the Valkyrie's card render.",
    "On 30/3/22, the Miner Update changed the card art of the Valkyrie.",
    "On 1/11/2016, the November 2016 Update, removed the word \"Ledoot\" from its description.",
    "On 2/9/2021, a maintenance break, changed the Skeleton Army's card render.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Bomber from Training Camp (Tutorial) to Bone Pit (Arena 2).",
    "On 2/9/2021, a maintenance break, changed the Musketeer's card render.",
    "On 5/9/2018, the September 2018 Update, changed it so that Epic cards start at level 6 and end at level 13 (from 1 to 8). It also changed the Baby Dragon's card description. It used to read \"Flying troop that deals area damage. Baby dragons hatch cute, hungry and ready for a barbeque.\"",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Baby Dragon from Training Camp (Tutorial) to Bone Pit (Arena 2).",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Prince from Training Camp (Tutorial) to Royal Arena (Arena 7).",
    "On 7/7/2020, a Balance Update, changed the Wizard's card render.",
    "On 5/9/2018, the September 2018 Update, changed it so that Rare card start at level 3 and end at level 13 (from 1 to 11).",
    "On 7/4/2020, a Balance Update, added a card render to the Mini P.E.K.K.A's card info screen.",
    "On 1/7/22, a maintenance break changed the Mini P.E.K.K.A's card image.",
    "On 30/7/2020, a maintenance break, added a card render to the Spear Goblins' card info screen.",
    "On 1/11/2016, the November 2016 Update, changed the Giant Skeleton's sound effects, and he now laughs when deployed.",
    "On 5/8/2019, a Balance Update, removed the Giant Skeleton from all Draft selections.",
    "On 3/6/22, a maintenance break changed the Giant Skeleton card icon and card render.",
    "On 1/4/2016, certain Content Creators were given a different version of the game, with a Tombstone that visually looked larger and would spawn Giant Skeletons instead of Skeletons.",
    "On 22/11/2017, a maintenance break, temporarily removed the Hog Rider from the Touchdown mode.",
    "On 26/11/2019, the End of November 2019 Update, removed the Hog Rider from Mega Deck Touchdown.",
    "On 2/9/2021, a maintenance break, changed the Hog Rider's card render.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Minion Horde from P.E.K.K.A's Playhouse (Arena 4) to Hog Mountain (Arena 10).",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Ice Wizard from Spell Valley (Arena 5) to Frozen Peak (Arena 8).",
    "On 7/7/2020, a Balance Update, changed the Ice Wizard's card render.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Ice Wizard.",
    "On 2/9/22, a maintenance break changed the Royal Giant's card icon and added a card render to the Royal Giant's card info screen.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Guards from Royal Arena (Arena 7) to Spooky Town (Arena 12).",
    "On 2/9/2021, a maintenance break, changed the Guards' card render.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Princess from Royal Arena (Arena 7) to Spell Valley (Arena 5).",
    "On 2/9/2021, a maintenance break added a card render to the Dark Prince's card info screen.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Lava Hound from P.E.K.K.A's Playhouse (Arena 4) to Hog Mountain (Arena 10).",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Lava Hound.",
    "On 19/9/2016, the September 2016 Update, changed the walking animation of the Ice Spirit.",
    "On 3/2/2020, the February 2020 Update, added a card render to the Ice Spirit's card info screen.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Miner from Builder's Workshop (Arena 6) to P.E.K.K.A's Playhouse (Arena 4).",
    "On 7/10/2019, a maintenance break, added a new Star Level.",
    "On 7/6/2021, the 2021 Quarter 2 Update added the blurb \"A shovel that deals reduced damage to Crown Towers.\" to his description.",
    "On 2/9/2021, a maintenance break, changed the Miner's card render.",
    "On 4/7/2016, the Tournaments Update, changed her description. It used to read \"Sparky has a heavy-handed approach in life: Obliterate everything in sight.\"",
    "On 19/9/2016, the September 2016 Update, changed her description. It used to read \"With coils of iron and wheels of wood, the Sparky unloads massive damage to opponents. Overkill isn't in her dictionary.\"",
    "On 1/11/2016, the November 2016 Update, changed her description slightly. It used to read \"Sparky slowly charges up, then unloads MASSIVE area damage. Overkill isn't in her dictionary\".",
    "On 2/9/2021, a maintenance break added a card render to the Sparky's card info screen.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Sparky.",
    "On 19/9/2016, the September 2016 Update, changed his description. The description used to say \"This big blue dude digs the simple things in life - Dark Elixir drinks and throwing rocks. His massive boulders bounce off their target, landing behind for a double strike.\"",
    "On 1/11/2016, the November 2016 Update, changed the Bowler's sound effects."
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Bowler from Frozen Peak (Arena 8) to Rascal's Hideout (Arena 13).",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Lumberjack from Frozen Peak (Arena 8) to Serenity Peak (Arena 14).",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Lumberjack.",
    "On 28/5/2020, a maintenance break, added a card render to the Battle Ram's card info screen.",
    "On 12/6/2017, the Battle Ram was supposed to receive a change where fatal damage to the Battle Ram would not deal damage to the Barbarians as well, but this change was pulled back last minute.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Inferno Dragon from P.E.K.K.A's Playhouse (Arena 4) to Builder's Workshop (Arena 6).",
    "On 28/5/2020, a maintenance break, added a card render to the Inferno Dragon's card info screen.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Inferno Dragon.",
    "On 3/2/2020, the February 2020 Update, added a card render to the Ice Golem's card info screen.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Ice Golem.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Mega Minion from Royal Arena (Arena 7) to P.E.K.K.A's Playhouse (Arena 4).",
    "On 28/4/22, a maintenance break added a card render to the Mega Minions's card info screen.",
    "On 25/4/2018, the Clan Wars Update, increased the Dart Goblin’s damage by 3%. The update also slightly changed his description. It used to read “Runs fast, shoots far and chews gum. How does he blow darts with a mouth full of gum? Years of didgeridoo lessons.”. This was due to the release of the Rascals and their description, \"Spawns a mischievous trio of Rascals! The boy takes the lead, while the girls pelt enemies from behind… with slingshots full of Double Trouble Gum!\"",
    "On 30/3/22, the Miner Update changed the Dart Goblin's card render.",
    "On 4/8/2020, a Balance Update, added a card render to the Goblin Gang's card info screen.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Goblin Gang.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Electro Wizard from Royal Arena (Arena 7) to Electro Valley (Arena 11).",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Electro Wizard.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Elite Barbarians from Royal Arena (Arena 7) to Hog Mountain (Arena 10).",
    "On 2/9/2021, a maintenance break added a card render to the Elite Barbarians' card info screen.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Hunter from Jungle Arena (Arena 9) to Goblin Stadium (Arena 1).",
    "On 12/6/2017, the June 2017 Update, changed the sound effect of his axe throw.",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Executioner from Jungle Arena (Arena 9) to Spooky Town (Arena 12).",
    "On 2/9/2021, a maintenance break added a card render to the Executioner's card info screen.",
    "On 7/6/21, the 2021 Quarter 2 Update fixed a bug where the Bandit's dash would continue after the timer reaches zero. It also moved the Arena to unlock the Bandit from Jungle Arena (Arena 9) to Rascal's Hideout (Arena 13).",
    "On 5/9/2018, the September 2018 Update, changed the Royal Recruits' sound effects. Previously, their sound effects were identical to those of the Guards.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Night Witch from Frozen Peak (Arena 8) to Spell Valley (Arena 5).",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Night Witch from Spell Valley (Arena 5) to Serenity Peak (Arena 14).",
    "On 30/9/22, a maintenance break changed the Night Witch's card image.",
    "On 9/10/2017, the Epic Quests Update, changed the card description. Prior to this update, it read \"Five tiny flying creatures with big ears. Having big ears doesn't mean they'll listen when asked to stop attacking you\".",
    "On 25/4/2018, the Clan Wars Update, changed the description; it used to read \"Spawns a handful of tiny flying creatures with big ears. Having big ears doesn't mean they're good listeners.\"",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Bats from Frozen Peak (Arena 8) to Spell Valley (Arena 5).",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Royal Ghost from Hog Mountain (Arena 10) to Royal Arena (Arena 7).",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Royal Ghost from Royal Arena (Arena 7) to Spooky Town (Arena 12).",
    "On 3/12/2019, a maintenance break, changed the Royal Ghost's card info localization.",
    "On 28/1/2019, the January 2019 Update, changed the Ram Rider's card description. It used to read \"Her bola snares enemy troops while Ram heads for the nearest building! Rams and Hogs don't mingle at parties…\"",
    "On 17/5/2019, the Ram Rider's card image was updated. The new image replaces the old image upon a new install; keeping the app installed prior to the update retains the old card image, even if the app is updated.",
    "On 26/11/2019, the End of November 2019 Update, removed the Ram Rider from Mega Deck Touchdown.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Cannon Cart from Hog Mountain (Arena 10) to Builder's Workshop (Arena 6).",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Cannon Cart from Builder’s Workshop (Arena 6) back to Hog Mountain (Arena 10).",
    "On 31/10/2017, the Skeleton Barrel became obtainable by achieving 9 wins in the Halloween Draft Challenge.",
    "On 23/11/2017, a maintenance break, temporarily removed the Skeleton Barrel from the Touchdown mode due to a bug where scoring a touchdown did not clear flying barrels from the arena, which break into Skeletons to score another touchdown while the opponent is unable to defend against it.",
    "On 12/1/2018, the Skeleton Barrel was added back to the Touchdown mode, the glitch presumably fixed.",
    "On 10/9/2020, an Optional Update, made it so that a cloned Skeleton Barrel would now function correctly.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Skeleton Barrel from Builder's Workshop (Arena 6) to Spooky Town (Arena 12).",
    "On 9/10/2017, the Epic Quests Update, changed the artwork of the Flying Machine card.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Flying Machine from Jungle Arena (Arena 9) to Builder's Workshop (Arena 6).",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Flying Machine.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Wall Breakers from Training Camp (Tutorial) to Spell Valley (Arena 5).",
    "On 27/6/2018, an Optional Update, fixed a Royal Hogs crash.",
    "On 26/11/2019, the End of November 2019 Update, removed the Royal Hogs from Mega Deck Touchdown.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Fisherman from Hog Mountain (Arena 10) to Legendary Arena (Arena 15).",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Magic Archer from Hog Mountain (Arena 10) to Spell Valley (Arena 5).",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Magic Archer from Spell Valley (Arena 5) to Rascal's Hideout (Arena 13).",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Electro Dragon.",
    "On 4/2/2020, a Balance Update, added the Firecracker to Clan Wars Collection Day card pool, Draft selections, and Mega Deck Touchdown.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Firecracker from Hog Mountain (Arena 10) to Serenity Peak (Arena 14).",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Firecracker.",
    "On 11/10/2019, a Tournament/Special Event Challenges allowed players to unlock the Elixir Golem early.",
    "On 3/12/2019, a maintenance break, changed the Battle Healer's card info localization. The card description for the Battle Healer was also changed slightly. It used to say, \"With each attack, she unleashes a powerful healing aura that restores Hitpoints to friendly Troops. Outside of combat she passively heals herself!\"",
    "On 20/1/2020, a maintenance break, added a card render to the Battle Healer's card info screen.",
    "On 31/8/2020, the Clan Wars II Update, changed the Battle Healer's card info screen.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Battle Healer.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Skeleton Dragons from Spooky Town (Arena 12) to P.E.K.K.A's Playhouse (Arena 4).",
    "On 15/4/2019, the April 2019 Update, changed the Goblin Hut's card image and also added an extra Star Level. The card's description flavour text was also changed slightly. It used to read \"Building that spawns Spear Goblins. But don't look inside. You don't want to see how they are made.\"",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Goblin Hut from Goblin Stadium (Arena 1) to Jungle Arena (Arena 9).",
    "On 3/6/22, a maintenance break changed the Goblin Hut's card render.",
    "On 25/4/2018, the Clan Wars Update, changed the Mortar's card description. It used to read \"Defensive building with a long range. Shoots exploding boulders that deal area damage. Cannot shoot at targets that get very close!\"",
    "On 15/4/2019, the April 2019 Update, changed the Mortar's card image.",
    "On 1/4/2016, certain Content Creators were given a different version of the game, with a Mortar that attacked by shooting Goblin Barrels instead of boulders.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Bomb Tower from Hog Mountain (Arena 10) to Spooky Town (Arena 12).",
    "On 3/6/22, a maintenance break added a card render to the Bomb Tower's card info screen.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Barbarian Hut from Barbarian Bowl (Arena 3) to Serenity Peak (Arena 14).",
    "On 15/4/2019, the April 2019 Update, changed the Tesla's card image.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Elixir Collector from Builder's Workshop (Arena 6) to Frozen Peak (Arena 8).",
    "On 1/4/2016, certain Content Creators were given a different version of the game, with an X-Bow that could also target friendly troops and buildings if they were in range.",
    "On 3/6/22, a maintenance break added a card render to the Tombstone's card info screen.",
    "On 1/4/2016, certain Content Creators were given a different version of the game, with a Tombstone that visually looked larger and would spawn Giant Skeletons instead of Skeletons.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Furnace.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Goblin Cage from Spooky Town (Arena 12) to Goblin Stadium (Arena 1).",
    "On 29/3/22, the Miner Update, made the Goblin Cage's rattling visual effect apply all the time. Previously it would only rattle when an enemy ground troop is nearby.",
    "On 29/2/2016, the March 2016 Update, changed the card's image.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Rage from Spell Valley (Arena 5) to Hog Mountain (Arena 10).",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Rage.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Rocket from Barbarian Bowl (Arena 3) to Builder's Workshop (Arena 6).",
    "On 11/10/2017, a maintenance break, temporarily removed the Goblin Barrel from the Touchdown mode due to a bug where scoring a touchdown did not clear flying barrels from the arena, which break into Goblins to score another touchdown while the opponent is unable to defend against it.",
    "On 1/4/2016, certain Content Creators were given a different version of the game, with a Mortar that attacked by shooting Goblin Barrels instead of boulders.",
    "On 3/5/2016, the May 2016 Update, changed the visual effects of the Freeze.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Freeze from P.E.K.K.A's Playhouse (Arena 4) to Spell Valley (Arena 5).",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Freeze from Spell Valley (Arena 5) to Frozen Peak (Arena 8).",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Mirror from Electro Valley (Arena 11) to Spooky Town (Arena 12).",
    "On 26/11/2019, the End of November 2019 Update, gave the Mirror a new animation if a card has been Mirrored. A Mirror appears on the ground with the new card, in addition to a special sound effect.",
    "On 30/3/21, a shadow Update erroneously removed the Mirror's visual and sound effects.",
    "On 7/6/21, an Update re-added Mirror's visual and sound effects as a bug fix.",
    "On 27/10/21, the 2021 Quarter 3 Update added the Level 14 Mirror. This, in turn, allowed it to spawn Level 15 cards.",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Lightning from Goblin Stadium (Arena 1) to P.E.K.K.A's Playhouse (Arena 4).",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Lightning from P.E.K.K.A's Playhouse (Arena 4) to Frozen Peak (Arena 8).",
    "On 20/6/2018, the Summer 2018 Update, moved the Arena to unlock the Zap from Spell Valley (Arena 5) to P.E.K.K.A's Playhouse (Arena 4).",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Zap from P.E.K.K.A's Playhouse (Arena 4) to Spell Valley (Arena 5).",
    "On 28/4/22, a maintenance break added a card render to the Zap's card info screen.",
    "On 3/5/2016, the May 2016 Update, changed the description of the Poison. The description prior to this update was \"Covers the target area in a sticky toxin, damaging and slowing down troops and buildings. Remember: solvent abuse can kill!\"",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Poison from Spell Valley (Arena 5) to Jungle Arena (Arena 9). It also slightly changed the Poison's description, adding the phrase \"Reduced damage to Crown Towers.\" to it.",
    "On 1/11/2016, the Novermber 2016 Update, changed the Graveyard's description to its current description. Prior to this, its description was \"Unearths a gang of Skeletons anywhere in the Arena. Spooky!\"",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Graveyard from Spell Valley (Arena 5) to Spooky Town (Arena 12).",
    "On 3/6/22, a maintenance break added a card render to the Graveyard's card info screen.",
    "On 7/4/2020, a Balance Update, added a card render to The Log's card info screen.",
    "On 7/6/21, the 2021 Quarter 2 Update slightly changed The Log's description, adding the phrase \"Reduced damage to Crown Towers.\" to it.",
    "On 28/1/2019, the January 2019 Update, moved the Arena to unlock the Tornado from Frozen Peak (Arena 8) to Spell Valley (Arena 5).",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Tornado from Spell Valley (Arena 5) to Legendary Arena (Arena 15). It also added a card render to the Tornado's card info screen.",
    "On 1/7/2019, the July 2019 Update, removed the Clone from all Draft selections.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Clone from Electro Valley (Arena 11) to Legendary Arena (Arena 15).",
    "On 30/3/22, the Miner Update added a card render to the Clone's card info screen.",
    "On 31/8/2020, the Clan Wars II Update, changed the Earthquake's card info screen.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Earthquake from Jungle Arena (Arena 9) to Spooky Town (Arena 12).",
    "On 28/4/22, a maintenance break added a card render to the Earthquake's card info screen.",
    "On 31/8/2020, the Clan Wars II Update, changed the Heal Spirit's card info screen.",
    "On 27/10/21, the 2021 Quarter 3 Update added the level 14 Heal Spirit.",
    "On 2/7/2018, a Balance Update, added the Giant Snowball to Clan Wars Collection Day card pool.",
    "On 7/6/21, the 2021 Quarter 2 Update slightly changed the Giant Snowball's description, adding the phrase \"Reduced damage to Crown Towers.\" to it.",
    "On 7/6/21, the 2021 Quarter 2 Update moved the Arena to unlock the Royal Delivery from Spooky Town (Arena 12) to Legendary Arena (Arena 15)."
}

skipped_keywords = {
    "increased the level cap of all cards to 14",
}

def keyword_contained_in(text):
    for keyword in skipped_keywords:
        if keyword in text:
            return True
    return False

def add_leading_zero_if_needed(num):
    if len(num) == 1:
        num = "0" + num
    return num


def convert_date_with_digits(date):
    split_date = date.split('/')

    split_date[0] = add_leading_zero_if_needed(split_date[0])
    split_date[1] = add_leading_zero_if_needed(split_date[1])
    if len(split_date[2]) == 2:
        split_date[2] = "20" + split_date[2]

    return split_date[0] + "/" + split_date[1] + "/" + split_date[2]


def convert_date_with_alphabets(date):
    map_month_name_to_number = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    split_date = date.split(' ')

    day = add_leading_zero_if_needed(split_date[0])
    month = map_month_name_to_number[split_date[1]]
    month = add_leading_zero_if_needed(month)
    year = split_date[2]
    return day + "/" + month + "/" + year

def is_valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False
