import sys

from aitextgen import aitextgen

ai = aitextgen(model_folder="dril-heroicvillain95",
               to_gpu=True)


def generateMessage(message):
    strTokens = message.strip().split(" ")
    strTokensLen = len(strTokens)
    minlength = int(strTokensLen * 2)
    minlength = 5 if minlength < 5 else minlength
    maxlength = strTokensLen * 10
    maxlength = 150 if maxlength > 150 else maxlength
    genprompt = ' '.join(strTokens).strip()
    statstext = "Stats: prompt=\"%s\" seed:%d, temperature=1.0, do_sample=True, " \
                "top_p=0.9, top_k=50, no_repeat_ngram_size=2 " \
                "max_length=%d, min_length=%d" % (genprompt, int(sys.argv[2]), maxlength, minlength)
    try:
        print(ai.generate_one(prompt=genprompt, temperature=1.0, do_sample=True,
                              repetition_penalty=1.1, top_p=0.9, top_k=50,
                              max_length=maxlength, min_length=minlength,
                              seed=int(sys.argv[2]), no_repeat_ngram_size=2)
              + "\n||[%s]||" % statstext)
    except Exception as e:
        print("Error occurred during generation. ||Error: %s [Stats: %s]||" % (e, statstext))


def main():
    # while True:
    #     prompt = input("Enter prompt(Exit to quit)")
    #     if prompt == "Exit":
    #         break
    generateMessage(sys.argv[1])


if __name__ == '__main__':
    main()
