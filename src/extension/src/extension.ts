import { commands, ExtensionContext, Uri, workspace, window } from "vscode";
import * as path from "path";
import { Controller } from "./controller";

export function activate(context: ExtensionContext) {
  context.subscriptions.push(
    commands.registerCommand(
      "webTemplateStudioExtension.wizardLaunch",
      async () => {
        Controller.getInstance(context, Date.now());
      }
    )
  );

  const readme = commands.registerCommand(
    "webTemplateStudioExtension.openReadme",
    async () => {
      const workspaceInfo = workspace.workspaceFolders;
      if (workspaceInfo) {
        const readmePath = path.join(workspaceInfo[0].uri.fsPath, "README.md");
        const doc = await workspace.openTextDocument(Uri.file(readmePath));
        await window.showTextDocument(doc, { preview: false });
        commands.executeCommand("markdown.showPreview", Uri.file(readmePath));
      }
    }
  );
  context.subscriptions.push(readme);
}

export function deactivate() {
  Controller.dispose();
}
