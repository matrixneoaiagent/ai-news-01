from pathlib import Path

SUMMARY = "Russia and Ukraine agreed a large prisoner exchange at US-mediated talks in Abu Dhabi, the biggest humanitarian release since the war began in 2022, but the talks ended without a breakthrough on post-war security. Democrat Scott Colom defeated Republican incumbent Cindy Hyde-Smith in Mississippi's US Senate race, becoming the first Black senator elected from the state since 1875 and the first Democrat since 1982, after more than a week of ballot counting. Spain's first general strike in 14 years shut businesses and disrupted transport as millions protested housing costs; tens of thousands marched in Madrid and Barcelona, and clashes broke out in Barcelona. Congo's deadliest Ebola outbreak passed 11,000 cases while Kenya discharged its last Ebola patient and began a 42-day countdown to being declared Ebola-free. The US House voted 211-204 to refer articles of impeachment against Defence Secretary Pete Hegseth to the Judiciary Committee, effectively ending the effort, though Democrats can try again next year. Federal prosecutors charged three men accused of being Iran-backed operatives over nearly 20 attacks, including a plot at RAF Fairford, a UK base housing US troops; a US soldier is separately held in the UK on Russian spying claims. Nvidia's board hired the law firm Wachtell, Lipton, Rosen & Katz, led by partner Joon Kim, to investigate chief executive Jensen Huang's relationship with an alleged Chinese spy. Two trains collided near Cairo, killing at least seven people and injuring more than 125, prompting an investigation. A Kenyan court jailed doomsday sect leader Paul Mackenzie for 200 years for the murders of 190 children whose followers were ordered to starve. South Africa's ANC was on course for a double-digit drop in local elections with 80% of ballots counted, while flash floods killed people in northern Iraq and Ukraine captured its first Indonesian prisoner of war. US envoys are due to meet Vladimir Putin and Volodymyr Zelensky on Thursday."


def main():
    entry = Path("/output/entry.txt")
    entry.parent.mkdir(parents=True, exist_ok=True)
    entry.write_text(SUMMARY, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
