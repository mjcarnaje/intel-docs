import logging

from langchain_core.prompts import ChatPromptTemplate

from ..services.ollama import LLM

logger = logging.getLogger(__name__)

class DocumentProcessor:
    """
    Handles text processing, including summary and title generation for documents.
    """

    @staticmethod
    def generate_summary(text: str) -> str:
        """
        Generate a detailed summary of the provided text using a language model.

        Args:
        text: The text extracted from the document.

        Returns:
            A summary string.
        """

        
        summary_template = (
            "You are an expert document analyst. Your task is to read the following text and provide a concise yet comprehensive summary. "
            "Focus on the main ideas, key points, and essential information. Ensure the summary is clear and accurately reflects the document's content.\n\n"
            "Text: {text}\n\n"
            "Summary:"
        )
        prompt = ChatPromptTemplate.from_template(summary_template)
        summary = (prompt | LLM).invoke({"text": text})
        logger.info("Summary generated successfully.")
        return summary

    @staticmethod
    def generate_title(summary: str) -> str:
        """
        Generate a title for the document based on its summary.

        Args:
            summary: The summary of the document content.

        Returns:
            A title string.
        """
        title_template = (
            "You are a professional title creator. Based on the following summary, create a short, concise, and informative title that accurately represents the content. "
            "The title should be no more than 500 characters long, clear, descriptive, and free of any special formatting or markdown syntax.\n\n"
            "Summary: {summary}\n\n"
            "Title:"
        )
        prompt = ChatPromptTemplate.from_template(title_template)
        title = (prompt | LLM).invoke({"summary": summary})
        logger.info("Title generated successfully.")
        return title
