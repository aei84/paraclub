class RegistrationRequest(PersonMixin, BaseModel):
    __tablename__ = "registration_requests"

    registration_status: Mapped[RegistrationStatus]