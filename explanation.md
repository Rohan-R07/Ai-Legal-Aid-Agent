Thank you for providing the detailed terminal log! This output is exactly what I needed, and it clearly shows the problem.

The critical part of the error message is:
`Quota exceeded for metric: generativelanguage.googleapis.com/embed_content_free_tier_requests, limit: 0, model: embedding-001`

**This means that your Google API key has a quota limit of ZERO for the embedding service.**

Even with all the batching and delays I've implemented, if your quota for this specific service (`embedding-001` model) is set to 0, no embedding requests will succeed. This is an issue with your Google Cloud project setup and not with the application's code itself.

**To resolve this, you will need to do the following:**

1.  **Go to your Google Cloud Console:** Log in to the Google Cloud Console where you generated your API key.
2.  **Navigate to the Gemini API / Generative Language API:** Find the section related to the Gemini API or Generative Language API.
3.  **Check Quotas and Billing:**
    *   **Verify Quotas:** Look for the "Quotas" section. Specifically, check the quotas for the `embedding-001` model and the "EmbedContentRequests" metric. It currently shows a limit of 0. You might need to request a quota increase.
    *   **Check Billing:** Ensure that billing is enabled for your project, as some higher quotas might require an active billing account. Even if you're using the free tier, sometimes an enabled billing account is a prerequisite for certain quota limits.
4.  **Consider a New API Key:** If you've been having persistent issues, sometimes generating a brand new API key within a project that has active quotas can help.

Unfortunately, this is an external configuration issue that I cannot fix through code changes. Once you've adjusted your API key's quotas in the Google Cloud Console, the application should work as expected.

Please let me know once you've checked and adjusted your API quotas.
