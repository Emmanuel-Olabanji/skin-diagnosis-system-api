from fastapi import HTTPException, status


class EmailService:
    @staticmethod
    def send_email(to_email: str, subject: str, message: str) -> bool:
        # Placeholder service for production email integration
        if not to_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Recipient email is required.",
            )
        return True
