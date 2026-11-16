# Produce crop ranking (2026-11-16)

Source: `data/processed/produce_crop_economics.csv`, best channel per crop at the FAMILY
labor rate ($11/hr loaded). Net per acre is after paying family wages; family income adds
those wages back. Confidence is low to medium throughout: prices are regional proxies, not
Wichita observations, and no Kansas trial exists for several crops. Stage-1 acres are the
files' recommendations, bounded by channel ceilings and labor.

## By net per acre (descending)
| Rank | Crop | Best channel | Net $/acre | Net $/labor hr | Family income $/acre | Stage-1 acres | Mechanized | Stores (mo) | Top disqualifier |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Cut flowers | florists / events | 64,600 | 40 | 82,200 | 0.25 | no | 0 | no one for 3 harvest mornings/week + Saturdays May–Oct; Wichita florist channel caps ~0.3–0.4 ac |
| 2 | Tomatoes | market / CSA (chef close) | 26,300 | 44 | 35,150 | 0.25 + tunnel | no | 0 | no dedicated picker 20 hr/wk Jun–Oct; picking overlaps wheat harvest |
| 3 | Peppers | market / CSA (chef close) | 18,200 | 42 | 24,600 | 0.25 | no | 0 | companion to tomatoes only; wholesale bells lose to $1/lb imports |
| 4 | Melons | chef-direct | 13,000 | 74 | 15,200 | 0.5 | no | 0 | needs sandy loam, legal irrigation and a July–Aug person; chef ceiling ~0.5 ac |
| 5 | Pumpkins and winter squash | chef-direct cured squash | 10,200 | 131 | 11,150 | 2.0 | partial | 3 | u-pick on trust land (liability, trustee); unsold jacks after Nov 1 |
| 6 | Onions and garlic | market / CSA; garlic alone far higher | 8,000 | 31 | 12,450 | 0.75 | partial | 7 | bloat nematode or white rot ends the seed-garlic channel; year-1 seed garlic cost |
| 7 | Sweet potatoes | chef-direct | 4,000 | 29 | 6,500 | 0.5 | partial | 8 | no warm curing zone (55–60°F) means an October dump |
| 8 | Sweet corn | chef-direct (market scales) | 4,000 | 52 | 5,000 | 1.5 | partial | 0 | no irrigation for July silking; raccoons and earworm |
| 9 | Potatoes | chef-direct | 3,700 | 29 | 6,000 | 0.75 | partial | 6 | dig collides with wheat harvest; scab on high-pH soil |
| 10 | Green beans | market / CSA | 3,600 | 7 | 9,100 | 0.25 | partial | 0 | hand picking worth $6–7/hr, below hired wage; wholesale negative |

## By net per labor hour (descending)
Pumpkins and squash 131 · melons 74 · sweet corn 52 · tomatoes 44 · peppers 42 · cut
flowers 40 · onions and garlic 31 · sweet potatoes 29 · potatoes 29 · green beans 7.

## Readings
- Per acre, the hand-picked crops win (flowers, tomatoes, peppers) but each is capped by
  a channel ceiling or by one person's picking hours, so the right unit is a quarter acre
  or a tunnel, not acres.
- Per labor hour, the mechanizable field crops win (pumpkins and squash, melons, sweet
  corn), which suits a farm with tractors and no dedicated labor.
- Storables (garlic, onions, sweet potatoes, potatoes, squash) earn less per acre but sell
  October to April when local supply is thin and spread labor away from summer peaks.
  Hardneck garlic alone is the standout: ~$16,600/acre and $68/hr, and it survives every
  adverse case in its file.
- Switching from family to hired labor cuts net by 15–40% on hand-picked crops and turns
  green beans and wholesale channels to zero or negative.
- Grocery and wholesale is the worst channel for every crop at this scale.

## A stage-1 portfolio that fits the constraints (about 3.5 acres, one family member part time plus Tony's equipment)
| Crop | Acres | Expected family income | Why |
|---|---|---|---|
| Cut flowers | 0.25 | ~$14–20k | highest value; florists plus market |
| Tomatoes (tunnel + field) and peppers | 0.5 | ~$15–20k | chef and market anchor, if the picker exists |
| Pumpkins and winter squash | 1.5 | ~$12–15k | tractor work, fall market, chef squash |
| Garlic (0.25) and onions (0.5) | 0.75 | ~$8–10k | winter sales, mechanized dig |
| Sweet corn | 0.5 | ~$2–3k | market draw, succession after wheat harvest |
Total roughly $50–65k family income on 3.5 acres at the family wage, against ~$1,000 as
grain. Drop tomatoes and flowers if no one can commit to summer picking; the remaining
2.75 acres still return ~$22–28k.

## Verify first
Wichita prices at Kansas Grown and Old Town markets in 2027; six chef letters of intent;
soil texture, pH and water right on the candidate plot; a committed family member's hours.
