airbnb_prompt = """ 
**ADVANCED HOTEL SEARCH FORMAT**

## 🎯 Search Summary
- **Location:** [location] | **Dates:** [checkin] → [checkout]
- **Guests:** [adults]A, [children]C, [infants]I, [pets]P
- **Room:** [room type] | **Stars:** [rating] | **Amenities:** [amenities]
- **Results:** [number] hotels

## 🏨 Hotel Listings
### [Hotel Name]
| Detail | Info |
|--------|------|
| ⭐ Rating | [rating]/5 ([reviews]) |
| 📍 Address | [full address] |
| 💰 Rate | $[price]/night (+$[tax]) |
| 🏠 Rooms | [categories] |
| 📏 Distance | [city center] • [airport] |
| 🔗 Booking | [URL] |
| 📞 Contact | [phone] • [website] |

**Amenities:** [pool/gym/spa, dining, transport, business, pets, WiFi, services]  
**Booking:** Check-in [time], Check-out [time], Cancellation [policy], Payment [methods], Breakfast [info], Parking [info], Extra Beds [policy]

**Match Analysis:** Budget [fit], Amenities [X/Y matched], Location [score], Guest Reviews [highlights]  
**Recommendations:** Best for [use case], Offers [promos], Tips [advice]

-- repeat per hotel --

## 📈 Comparison
| Hotel | Rating | Price | Features | Link |
|-------|--------|-------|----------|------|
| [H1] | [rating]⭐ | $[price] | [2 highlights] | [URL] |
| [H2] | [rating]⭐ | $[price] | [2 highlights] | [URL] |

## 🏆 Final Picks
- **Best Value:** [hotel + reason]
- **Luxury:** [hotel + features]
- **Budget:** [hotel + savings]
- **Location:** [hotel + benefit]
- **Amenities:** [hotel + standout]
"""
