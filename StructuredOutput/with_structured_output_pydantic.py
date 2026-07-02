from pydantic import BaseModel,Field
from typing import Literal,Optional
from pathlib import Path
from langchain_openai import ChatOpenAI



review = Path('movie_review.txt').read_text()

# schema of my pydantic
class Review(BaseModel):

    key_themes: list[str] = Field(description ='Write down all key themes discussed in review in a list')
    summary: str = Field(description='A brief summary of the review')
    sentiment: Literal['pos','neg'] = Field(description='Write sentiment of review as positive, negative or neutral')
    pros: Optional[list[str]] = Field(default = None,description='positive points about review, if any')
    cons: Optional[list[str]] = Field(default = None,description='write negative points about review, if any')
    name: Optional[str] = Field(default = None, description='Write name of the protoganist')

model = ChatOpenAI().with_structured_output(Review)
result = model.invoke(review)

print(result.key_themes)