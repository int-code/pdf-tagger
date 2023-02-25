import cohere
from dotenv import load_dotenv
import os
from nltk.corpus import stopwords


def gettags(prompt:str):

  load_dotenv()
  stopwords=stopwords.words('english')
  with open("adverbs.txt") as fp:
    stopwords+= fp.readlines()
  co = cohere.Client(os.getenv('COHERT_KEY'))
  # prompt="A cow is a pet. The importance of cows is considered all over the world, which is usually found everywhere. But if we talk about India, it plays an important role in the economy of India since ancient times. Whether it is a matter of milk or a dessert or food made with milk.In ancient times, having cows with anyone was considered a sign of prosperity. Apart from milk production, it is a very useful domestic animal. According to a report, India has a population of about 190 million cows.Use of cow:A cow is a pet, so it is commonly reared in homes. Cow’s milk is very nutritious. A cow gives usually five to ten liters of milk at a time. Sweets are made like buttermilk, butter, cheese, curd, and other milk are made from cow’s milk. It is considered a very useful diet for sick people and children.Cow milk is considered very beneficial as compared to other animals. When compared to buffalo and cow’s milk, where buffalo milk brings lethargy, while cow’s milk maintains versatility in children. Children are especially advised to feed cow’s milk by doctors and specialists.Cow dung is also used as fertilizer in fields. Apart from this, cow dung is dried and used in fuel work. The best fertilizer for crops. Cow urine is considered very sacred. Cow’s ghee and cow urine are used to make many ayurvedic medicines.The cow keeps giving something throughout its life. Even after death, every part of his body is used. Many artifacts are made from its bones. Cow’s leather, horns, hoofs are used daily to produce useful items. Manure prepared from cow bones is used for farming and its skins are dried and used as leather.Body composition of cow:The structure of the cow is found to be the same in all countries, but there is a difference in the height and breed of the cow. Some cows give more milk and some give less. The cow has two ears, four udder, one mouth, two eyes, two horns, and two nostrils.The cow is a four-legged animal and has hoofs on all four legs, hoofs of feet act as shoes for the cow. With which they can walk on any hard space.The tail of the cow is long and there is also a bunch on its edge, which she uses to fly flies etc. Some species of cow do not have horns. Only 32 teeth are found in the lower jaw of its mouth, so the cow chews for a long time by chewing food.Major breeds of cows:There are many breeds of cows all over the world, some of which give good milk and some have strong bodies. In India, there are mainly cow’s breeds such as Sahiwal (Punjab, Haryana, Delhi, Uttar Pradesh, and Bihar), Gir (South Kathiawar), Tharparkar (Jodhpur, Jaisalmer, and Kutch), Karan Fry (Rajasthan) etc.There are many types of cows in foreign countries too. Among which Jersey cow is the most popular. Because it gives more milk. Indian cows are smaller in size, while foreign cows have a slightly heavier body. The cow is of many colours such as red, black, white, drab.Religious importance of cow:In other countries, the cow is considered only a domestic animal, but in India, the cow has the status of a goddess. The cow was considered a symbol of prosperity in ancient India and present time as well. It is believed that 33 crore deities reside in the body of the cow.Cow shelter has been constructed by people and institutions in many places in India. Through which food is given to stray and injured cows and they are treated.Conclusion:Cow is peace loving and domesticated. Unfortunately, city condition is getting worse day by day, the way polythene is used and thrown away in cities. Cows die prematurely by consuming it. There is a need to think about which cow in our India has been given the status of mother because it keeps giving something throughout its life, so we should learn something from its life"

  response = co.summarize(
    text=prompt,
    model='summarize-xlarge',
    length='short'

  )


  summary=response.summary
  summary = [x for x in response.summary.split(" ") if not x.lower() in stopwords]

  for idx,x in enumerate(summary):
    # print(x, idx)
    summary[idx]=''.join([i.lower() for i in x if i not in [',','.','(',')','?', '-', ';', ':']])
    
  return set(summary)


if __name__=="__main__":
  gettags("aeuifhiabf qeuifahkeqa")